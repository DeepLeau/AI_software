import pyttsx3
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from diffusers import StableDiffusionPipeline
import torch


# Initialiser le modèle de chatbot
template = """
Answer the question below in English.

Here's the history of the conversation: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda" if torch.cuda.is_available() else "cpu")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def process_question(context: str, question: str) -> str:
    """Traite la question et génère une réponse en anglais."""
    result = chain.invoke({"context": context, "question": question})
    return result

#def speak(text):
    """Fait parler le chatbot avec pyttsx3."""
#    engine = pyttsx3.init()
#    engine.say(text)
#    engine.runAndWait()


def summarize_text(text: str)->str:
    question = "Can you summarize the following text ? Just provide the text nothing more, nothing less."
    context = f"Text: {text}"
    summary = process_question(context, question)
    return summary

def generate_image(prompt: str):
    """Generates an image from a text prompt."""
    image = pipe(prompt).images[0]
    image.save("generated_image.png")
    return "generated_image.png"