from fastapi import FastAPI
from pydantic import BaseModel
from nvemo import process_question, speak

app = FastAPI()

class QuestionRequest(BaseModel):
    context: str
    question: str

@app.post("/chat/")
async def chat(request: QuestionRequest):
    response = process_question(request.context, request.question)
    speak(response)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

