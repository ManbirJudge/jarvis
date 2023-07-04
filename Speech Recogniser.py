import datetime
import random

import pyttsx3
from googletrans import Translator

import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

random_voice = random.choice(voices)
random_voice_id = random_voice.id

engine.setProperty('voice', random_voice_id)

translator = Translator()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    recogniser = sr.Recognizer()

    with sr.Microphone() as microphone:
        print('Listening ...')

        recogniser.pause_threshold = 1
        audio = recogniser.listen(microphone)

    try:
        print('Recognising ...')

        query = recogniser.recognize_google(audio, language='hi-IN')
        hindi_query = translator.translate('query', dest='hi')

        print(f'\nUser Said: {hindi_query}\n')

    except Exception as e:
        print(f'\nError: {e}')
        print('\nSay That Again Please ...')

        query = 'None'

    return query.lower()


def wish():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak('Good Morning!')
    elif 12 <= hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am Jarvis. How can I help you?')


if __name__ == '__main__':
    wish()

    run = True

    while run:
        cmd = take_command()
