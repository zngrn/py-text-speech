import pyttsx3
from decouple import config
from datetime import datetime

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


if __name__ == "__main__":
    bot_speak('Hello! I am Cosmo!')
    bot_greet()