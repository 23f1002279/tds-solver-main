import csv
import json
from fastapi import FastAPI, HTTPException, Request
from typing import Optional, Dict, List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/api")
async def read_item(request: Request = None):
    query_params = request.query_params.getlist('class')
    classes = []
    for value in query_params:
        if value not in classes:
            classes.append(value)
    
    print(classes)
    output_list = []
    
    with open('q-fastapi.csv', mode='r') as file:
        csv_reader = csv.reader(file)

    
        for row in csv_reader:
            
            if row[1] in classes:
                output_list.append({
                    "studentId": int(row[0]),
                    "class": row[1]
                })
    
    return JSONResponse(content={"students": output_list})

    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)