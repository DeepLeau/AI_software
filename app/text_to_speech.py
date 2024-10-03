import pyttsx3
import speech_recognition as sr
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Réponds à la question ci-dessous en français.

Voici l'historique de la conversation: {context}

Question: {question}

Réponse en français:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="fr-FR")  
            print(f"Vous avez dit: {text}")
            return text
        except sr.UnknownValueError:
            print("Je n'ai pas compris")
            return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def test_speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chatbot_conversation():
    context = ""
    while True:
        user_input = capture_voice()
        # if user_input is None or user_input.lower() == "déconnecte-toi" or "déconnecte toi":
        #     break

        result = chain.invoke({"context": context, "question": user_input})
        print(f"Bot: {result}")
        speak(result) 
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    chatbot_conversation()
