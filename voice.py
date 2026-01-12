import speech_recognition as sr
import pyttsx3
from agent import agent

r=sr.Recognizer()
engine=pyttsx3.init()
user="baisnabi"

while True:
    with sr.Microphone() as src:
        print("Speak...")
        audio=r.listen(src)
        text=r.recognize_google(audio)
        print("You:",text)
        reply=agent(user,text)
        print("Agent:",reply)
        engine.say(reply)
        engine.runAndWait()
