from fastapi import FastAPI, HTTPException
from tools import question_solvers
import os

app = FastAPI(title="TDS Solver API")

@app.get("/")
def read_root():
    return {"message": "Welcome to TDS Solver API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Add more endpoints as needed for your solver functions

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
