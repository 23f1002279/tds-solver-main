import httpx
import hashlib
from tqdm import tqdm
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from bs4 import BeautifulSoup
import json

# def cached_get(url):
#     filename = hashlib.md5(url.encode('utf-8')).hexdigest()
#     path = os.path

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Make sure this covers your client's origin
    allow_credentials=True,
    allow_methods=["*"],  # Ensure this includes 'OPTIONS'
    allow_headers=["*"],  # Make sure the necessary headers are included
)

@app.get("/scrape")
async def scrape(country: str = Query(...)):
    '''Scrape the wikipedia page for a given country, write all the headings <h1>, <h2>, ...., <h6> in a markdown file. Generate a Markdown-formatted outline that reflects the hierarchical structure of the content.'''
    response = httpx.get(f'https://en.wikipedia.org/wiki/{country}')
    headings = []
    with open('response.html', 'w') as f:
        f.write(response.text)

    soup = BeautifulSoup(response.text, 'html.parser') 

    # Extract headings
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # Generate Markdown-formatted outline
    markdown_outline = ""
    for heading in headings:
        level = int(heading.name[1])
        if level == 1:
            markdown_outline += f"# {heading.text}\n\n"
        elif level == 2:
            markdown_outline += f"## {heading.text}\n\n"
        elif level == 3:
            markdown_outline += f"### {heading.text}\n\n"
        elif level == 4:
            markdown_outline += f"#### {heading.text}\n\n"
        elif level == 5:
            markdown_outline += f"##### {heading.text}\n\n"
        elif level == 6:
            markdown_outline += f"###### {heading.text}\n\n"

    with open('outline.md', 'w') as f:
        f.write(markdown_outline)
    
    return {"outline": markdown_outline}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8002)