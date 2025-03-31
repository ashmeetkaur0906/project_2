from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('questions.json', 'r') as file:
    QA_DB = json.load(file)

class QuestionRequest(BaseModel):
    question: str

@app.post("/api/")
async def answer_question(request: QuestionRequest):
    answer = QA_DB.get(request.question)
    if answer is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"answer": answer}
