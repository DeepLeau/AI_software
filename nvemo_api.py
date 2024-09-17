from fastapi import FastAPI
from pydantic import BaseModel
from nvemo import process_question

app = FastAPI()

class QuestionRequest(BaseModel):
    context: str
    question: str

@app.post("/chat/")
async def chat(request: QuestionRequest):
    response = process_question(request.context, request.question)
    return {"response": response}
