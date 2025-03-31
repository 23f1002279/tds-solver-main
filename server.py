import httpx
from fastapi import FastAPI, UploadFile, Form, File, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from typing import Annotated, Dict, Optional, List, Any, Tuple
# from sentence_transformers import SentenceTransformer
import tempfile
import os
from tools.question_templates import question_templates
from tools.question_solvers import *
from tools.solvers_descriptions import solvers_descriptions
from specific_extractor_functions import extractors
import re
import numpy as np
import json
import chromadb
import pickle
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File to cache embeddings
EMBEDDINGS_CACHE_FILE = "question_embeddings_cache.pkl"
# Alternative: Use ChromaDB
USE_CHROMADB = False
CHROMADB_COLLECTION_NAME = "question_templates"

def custom_openai_embedding_function(texts: List[str]) -> List[List[float]]:
    """Generate embeddings using OpenAI API with httpx"""
    # Check if texts is a single string and convert to list if needed
    if isinstance(texts, str):
        texts = [texts]
    
    # Ensure all items are strings
    texts = [str(text).strip() for text in texts if text]
    
    api_key = os.getenv('AIPROXY_TOKEN')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "input": texts,
        "model": "text-embedding-3-small"
    }
    
    # Using httpx instead of requests
    with httpx.Client(timeout=30.0) as client:
        response = client.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/embeddings",
            headers=headers,
            json=data
        )
    
    if response.status_code == 200:
        embeddings = [item['embedding'] for item in response.json()['data']]
        return embeddings
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

def load_or_create_embeddings(question_templates: Dict[str, str], force_refresh: bool = False) -> Dict[str, List[float]]:
    """Load embeddings from cache or generate new ones if needed"""
    question_embeddings = {}
    cache_file = Path(EMBEDDINGS_CACHE_FILE)
    
    # Try to load from cache if it exists and we're not forcing a refresh
    if cache_file.exists() and not force_refresh:
        try:
            with open(cache_file, 'rb') as f:
                cached_data = pickle.load(f)
                
            # Check if all templates are in the cache
            all_templates_cached = all(q_id in cached_data for q_id in question_templates)
            
            if all_templates_cached:
                print("Loaded embeddings from cache file")
                return cached_data
            else:
                print("Cache exists but doesn't contain all templates, regenerating...")
        except Exception as e:
            print(f"Error loading cache: {e}, regenerating...")
    
    # Generate embeddings for all templates
    print("Generating embeddings for question templates...")
    template_texts = []
    template_ids = []
    
    for q_id, q_statement in question_templates.items():
        clean_template = re.sub(r'\{\w+\}', "X", q_statement)
        template_texts.append(clean_template)
        template_ids.append(q_id)
    
    # Get embeddings in a single API call for efficiency
    embeddings = custom_openai_embedding_function(template_texts)
    
    # Map embeddings back to question IDs
    for i, q_id in enumerate(template_ids):
        question_embeddings[q_id] = embeddings[i]
    
    # Save to cache file
    with open(cache_file, 'wb') as f:
        pickle.dump(question_embeddings, f)
    print(f"Saved {len(question_embeddings)} embeddings to cache file")
    
    return question_embeddings

def setup_chromadb(question_templates: Dict[str, str], force_refresh: bool = False) -> chromadb.Collection:
    """Set up ChromaDB collection for question templates"""
    client = chromadb.Client()
    
    # Delete collection if forcing refresh
    if force_refresh:
        try:
            client.delete_collection(CHROMADB_COLLECTION_NAME)
            print(f"Deleted existing ChromaDB collection: {CHROMADB_COLLECTION_NAME}")
        except:
            pass
    
    # Get or create collection
    try:
        collection = client.get_collection(CHROMADB_COLLECTION_NAME)
        # Check if collection has all templates
        existing_ids = collection.get()["ids"]
        if all(str(q_id) in existing_ids for q_id in question_templates):
            print(f"Using existing ChromaDB collection with {len(existing_ids)} templates")
            return collection
        else:
            # Some templates missing, recreate collection
            client.delete_collection(CHROMADB_COLLECTION_NAME)
            print("Recreating ChromaDB collection with updated templates")
    except:
        print(f"Creating new ChromaDB collection: {CHROMADB_COLLECTION_NAME}")
    
    collection = client.create_collection(CHROMADB_COLLECTION_NAME)
    
    # Prepare data for batch addition
    ids = []
    documents = []
    template_texts = []
    
    for q_id, q_statement in question_templates.items():
        clean_template = re.sub(r'\{\w+\}', "X", q_statement)
        ids.append(str(q_id))
        documents.append(clean_template)
        template_texts.append(clean_template)
    
    # Get embeddings for all templates
    embeddings = custom_openai_embedding_function(template_texts)
    
    # Add to collection
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )
    
    print(f"Added {len(ids)} templates to ChromaDB collection")
    return collection

def identify_question_with_file_cache(problem_statement: str, question_embeddings: Dict[str, List[float]]) -> Tuple[Optional[str], float]:
    """Identify the most similar question template using file-cached embeddings"""
    # Replace numbers with X to focus on the structure of the question
    normalized_statement = re.sub(r'\b\d+(\.\d+)?\b', 'X', problem_statement)
    
    # Generate embedding for the input problem statement
    input_embedding = custom_openai_embedding_function(normalized_statement)[0]
    
    # Find the most similar question template
    max_similarity = -1
    best_match_id = None
    
    for q_id, q_embedding in question_embeddings.items():
        # Calculate cosine similarity
        similarity = np.dot(input_embedding, q_embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(q_embedding))
        
        if similarity > max_similarity:
            max_similarity = similarity
            best_match_id = q_id
    
    return best_match_id, max_similarity

def identify_question_with_chromadb(problem_statement: str, collection: chromadb.Collection) -> Tuple[Optional[str], float]:
    """Identify the most similar question template using ChromaDB"""
    # Replace numbers with X to focus on the structure of the question
    normalized_statement = re.sub(r'\b\d+(\.\d+)?\b', 'X', problem_statement)
    
    # Generate embedding for the input problem statement
    input_embedding = custom_openai_embedding_function(normalized_statement)[0]
    
    # Query the collection for the most similar template
    results = collection.query(
        query_embeddings=[input_embedding],
        n_results=1,
        include=["documents", "distances"]
    )
    
    if results["ids"] and results["ids"][0]:
        best_match_id = results["ids"][0][0]
        # ChromaDB returns distance, not similarity, so convert
        # (assuming Euclidean distance, convert to similarity)
        distance = results["distances"][0][0]
        # Convert distance to similarity (higher is better)
        similarity = 1 / (1 + distance)
        return best_match_id, similarity
    else:
        return None, 0.0

def identify_question(problem_statement: str, question_templates: Dict[str, str], force_refresh: bool = False) -> Tuple[Optional[str], float]:
    """Main function to identify the most similar question template"""
    if USE_CHROMADB:
        collection = setup_chromadb(question_templates, force_refresh)
        return identify_question_with_chromadb(problem_statement, collection)
    else:
        question_embeddings = load_or_create_embeddings(question_templates, force_refresh)
        return identify_question_with_file_cache(problem_statement, question_embeddings)

# model = SentenceTransformer('all-MiniLM-L6-v2')

# question_embeddings = {}
# for q_id, q_statement in question_templates.items():
    
#     clean_template = re.sub(r'\{\w+\}', "X", q_statement)
#     question_embeddings[q_id] = model.encode(clean_template)


# def identify_question(problem_statement: str) -> Tuple[Optional[int], float]:
#     # Replace numbers with X to focus on the structure of the question
#     normalized_statement = re.sub(r'\b\d+(\.\d+)?\b', 'X', problem_statement)
    
#     # Generate embedding for the input problem statement
#     input_embedding = model.encode(normalized_statement)
    
#     # Find the most similar question template
#     max_similarity = -1
#     best_match_id = None
    
#     for q_id, q_embedding in question_embeddings.items():
#         # Calculate cosine similarity
#         similarity = np.dot(input_embedding, q_embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(q_embedding))
        
#         if similarity > max_similarity:
#             max_similarity = similarity
#             best_match_id = q_id
    
#     return best_match_id, max_similarity




def extract_parameters(matched_ques_id, question):
    if matched_ques_id == 30:
        arguments = {"user_message": extractors.extract_user_message(question)}
        return arguments
    tools = [solvers_descriptions[matched_ques_id]]
    print(tools)
    try:
        response = httpx.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('AIPROXY_TOKEN')}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "user", 
                        "content": f"""{question}"""
                    }
                    ],
                "tools": tools,
                "tool_choice": "required",
            },
        )
        raw_res = response.json()
        print(raw_res)
        output = response.json()["choices"][0]["message"]
        res = {"name": output["tool_calls"][0]["function"]["name"] , "arguments": output["tool_calls"][0]["function"]["arguments"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
   
    fn = eval(res["name"])
    arguments = json.loads(res["arguments"])

    return arguments



    
@app.get("/")
def read_root():
    return {"message": "Welcome to TDS Solver API"}



@app.post("/api")
async def api(question: Annotated[str, Form()], file: List[UploadFile] | None = None):
    if file:
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, file[0].filename)

        if len(file) == 2:
            file_path_2 = os.path.join(temp_dir, file[1].filename)
            with open(file_path_2, "wb") as f:
                content = await file[1].read()
                f.write(content)
        
        with open(file_path, "wb") as f:
            content = await file[0].read()
            f.write(content)
        
    matched_ques_id, similarity = identify_question(question, question_templates)

    print(matched_ques_id, similarity)

    solver = eval(f"solver_{matched_ques_id}")
    params = extract_parameters(matched_ques_id, question)
    print(params)
    if file:
        params["file_path"] = file_path
        params["file_name"] = file[0].filename
        params["temp_dir"] = temp_dir
        if len(file) == 2:
            params["file_path_2"] = file_path_2
            params["file_name_2"] = file[1].filename
    answer = solver(**params)
    if file:
        os.remove(file_path)
        if len(file) == 2:
            os.remove(file_path_2)
        for root, dirs, files in os.walk(temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(temp_dir)
    return {"answer": answer}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True)