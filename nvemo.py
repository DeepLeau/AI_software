from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialiser le modèle et le prompt
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def process_question(context: str, question: str) -> str:
    """Traite la question et renvoie la réponse."""
    result = chain.invoke({"context": context, "question": question})
    return result
