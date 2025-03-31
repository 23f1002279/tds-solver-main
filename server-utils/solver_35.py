# /// script
# requires-python = "==3.12"
# dependencies = [
#   "chromadb==0.4.15",
#   "sentence-transformers",
#   "fastapi",
#   "uvicorn",
#   "pydantic",
#   "requests",
#   "httpx"
# ]
# ///


import os
import httpx

import requests
import json


def custom_openai_embedding_function(texts):
    api_key = os.getenv('AIPROXY_TOKEN')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "input": texts,
        "model": "text-embedding-3-small"
    }
    
    response = requests.post(
        "http://aiproxy.sanand.workers.dev/openai/v1/embeddings",
        headers=headers,
        data=json.dumps(data)
    )
    
    if response.status_code == 200:
        embeddings = [item['embedding'] for item in response.json()['data']]
        return embeddings
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
    



from fastapi import FastAPI
import uvicorn
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Make sure this covers your client's origin
    allow_credentials=True,
    allow_methods=["*"],  # Ensure this includes 'OPTIONS'
    allow_headers=["*"],  # Make sure the necessary headers are included
)

class Item(BaseModel):
    docs: list
    query: str
    

async def setup_vector_db():
    """Initialize Chroma DB with an embedding function."""
    
    client = chromadb.Client()
    collections = client.list_collections()
    for collection_name in collections:
        client.delete_collection(name=collection_name)
    collection = client.create_collection(
        name="documents",
        embedding_function=custom_openai_embedding_function
    )
    return collection

async def search_similar(collection, query: str, n_results: int = 3) -> list[dict]:
    """Search for documents similar to the query."""
    d = collection.query(query_texts=[query], n_results=n_results)
    return [
        {"id": id, "text": text, "distance": distance}
        for id, text, distance in zip(d["ids"][0], d["documents"][0], d["distances"][0])
    ]


@app.post("/similarity")
async def main(item: Item):
    collection = await setup_vector_db()

    # Add some documents
    collection.add(
        documents = item.docs,
        ids = [str(i) for i in list(range(1, len(item.docs)+1))]
        
    )

    # Search
    results = await search_similar(collection, item.query, n_results=3)
    print(results)

    matches = [res['text'] for res in results]

    return {"matches": matches}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)