from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from nvemo import process_question, summarize_text, generate_image
import pdfplumber


app = FastAPI()

# Allow CORS for your React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    context: str
    question: str

class ImageRequest(BaseModel):
    prompt: str

@app.post("/chat/")
async def chat(request: QuestionRequest):
    response = process_question(request.context, request.question)
    #speak(response)
    return {"response": response}

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_text = extract_text_from_pdf(file)

    summary = summarize_text(pdf_text)
    print(summary)
    return {"summary": summary}

def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file.file) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()
    return full_text

@app.post("/generate-image/")
async def generate_image_api(request: ImageRequest):
    try:
        image_url = generate_image(request.prompt)
        return {"image_url": f"http://127.0.0.1:8000/image-generation/{image_url}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


