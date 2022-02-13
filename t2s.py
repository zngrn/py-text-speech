import pyttsx3
import speech_recognition
from decouple import config
from datetime import datetime
from random import choice
from utils import working_on_it, apologies

USER = config('USER')
BOT = config('BOT')

engine = pyttsx3.init('nsss')
engine.setProperty('rate', 187)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def bot_speak(content):
    engine.say(content)
    engine.runAndWait()
    engine.stop()

def bot_greet():
    current_hour = datetime.now().hour
    
    if current_hour in range(6,12):
        bot_speak(f"Good Morning! {USER}")
    elif current_hour in range(12, 16):
        bot_speak(f"Good afternoon! {USER}")
    elif current_hour in range(16, 21):
        bot_speak(f"Good evening! {USER}")
    bot_speak(f"I'm {BOT}. How can I be of assistance?")

def bot_listen():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)
    
    try:
        print('Analysing and recognizing audio input...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            bot_speak(choice(working_on_it))
        else:
            print('If that\'s all, I\'ll take a bow...')
            exit()
    except Exception as e:
        print(e)
        bot_speak(choice(apologies))
        query = 'None'
    return query 


if __name__ == "__main__":
    bot_speak('Hello! I am Cosmo!')
    bot_greet()