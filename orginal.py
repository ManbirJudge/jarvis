# imports
import datetime
import random

import pyttsx3
import speech_recognition as sr
import wikipedia

# setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', random.choice(voices).id)


# util functions
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

        query = recogniser.recognize_google(audio, language='en-in')

        print(f'\nUser Said: {query}')

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


# main program logic
if __name__ == '__main__':
    wish()

    running = True

    while running:
        cmd = take_command()

        if 'search' in cmd:
            cmd = cmd.replace('search', '', 1)

            if 'wikipedia' in cmd:
                cmd = cmd.replace('wikipedia', '', 1).replace('for', '', 1)

                print(f'\nSearching Wikipedia for \"{cmd}\" ...')
                speak(f'Searching Wikipedia for \"{cmd}\"')

                results = wikipedia.summary(cmd, sentences=3)

                print(f'\nAccording to Wikipedia:\n{results}\n')

                speak('According to Wikipedia')
                speak(results)
