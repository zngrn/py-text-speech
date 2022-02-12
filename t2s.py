import pyttsx3
from decouple import config

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


if __name__ == "__main__":
    bot_speak('Hello! I am Cosmo!')