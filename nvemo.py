import pyttsx3
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialiser le modèle de chatbot
template = """
Answer the question below in English.

Here's the history of the conversation: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
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
