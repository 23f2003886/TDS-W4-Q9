from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TechDocs TypeScript RAG API")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Predefined Q&A mapping (proof-of-concept)
PREDEFINED_ANSWERS = {
    "what does the author affectionately call the => syntax": {
        "answer": "fat arrow",
        "sources": "https://github.com/basarat/typescript-book#arrow-functions"
    },
    "which operator converts any value into an explicit boolean": {
        "answer": "!!",
        "sources": "https://github.com/basarat/typescript-book#truthy-and-falsy"
    }
}

@app.get("/search")
def search(q: str = Query(..., description="Developer question")):
    q_lower = q.lower().strip()
    
    # Look for exact match in predefined answers
    if q_lower in PREDEFINED_ANSWERS:
        return PREDEFINED_ANSWERS[q_lower]
    
    # If not found, return default
    return {
        "answer": "No relevant excerpt found.",
        "sources": ""
    }
