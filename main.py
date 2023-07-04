from sys import exit as sys_exit
import os
import datetime
from typing import Any

import PySimpleGUI as PySG
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

# setting up pysimplegui
PySG.theme("systemDefault")

layout = [
    [PySG.Output(size=(50, 15), font='Courier 10')],
    [PySG.Button('Take Command', size=(13, 1), key='CMD')]
]

window = PySG.Window('J.A.R.V.I.S.', layout=layout, icon='icon.ico')

# setting up pyttsx3
engine = pyttsx3.init('sapi5', True)
voices = engine.getProperty('voices')

engine.setProperty('rate', 145)
engine.setProperty('voice', voices[0].id)

# setting up speech recognizer
recognizer = sr.Recognizer()
recognizer.pause_threshold = 1


# utility functions
def speak(text: str):
    engine.say(text)
    engine.runAndWait()


def listen() -> str | None:
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        command_query = recognizer.recognize_google(audio, language='en-in')
        print("\nUser:", command_query)

    except Exception as e:
        log(e, 'err')

        print("\nSay that again please. . .")
        speak("Say that again please. . .")

        return None

    return command_query


def jarvis_thought(msg: str):
    print(f'JARVIS: {msg}')
    speak(msg)


def greet():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour <= 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis, How can I help you?")


def log(msg: Any, type_: str):
    if type_ == 'err':
        print(f'[_ERROR_] {msg}')


# main program logic
if __name__ == '__main__':
    greet()
    app_running = True

    while app_running:
        event, value = window.read()

        if event == 'CMD':
            query = listen().lower()

            if 'hello jarves' in query:
                jarvis_thought('Hello')

            elif 'hello jarvis' in query:
                jarvis_thought('Hello!')

            elif 'hello' in query:
                jarvis_thought('Hello!')

            elif 'how are you' in query:
                jarvis_thought('I am fine. How are you?')

            elif 'i am fine' in query:
                jarvis_thought('Ok-ok, but now please give me a command.')

            elif 'i am also fine' in query:
                jarvis_thought('Ok-ok, but now please give me a command.')

            elif 'open google chrome' in query:
                jarvis_thought('Okay, opening Google.')

                try:
                    os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')
                except Exception:
                    jarvis_thought('Cannot find Google Chrome in your system.')

            elif 'according to wikipedia' in query:
                jarvis_thought('Searching Wikipedia ...')

                query = query.replace('according to wikipedia', '')
                result = wikipedia.summary(query, sentences=2)

                jarvis_thought('According to wikipedia ...')
                jarvis_thought(result)

            elif 'open youtube' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('youtube.com')

            elif 'open google maps' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('maps.google.com')

            elif 'open gmail' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('gmail.com')

            elif 'open google docs' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('docs.google.com')

            elif 'open google sheets' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('sheets.google.com')

            elif 'open google slides' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('slides.google.com')

            elif 'open tribune epaper' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('epaper.tribuneindia.com')

            elif 'open google translator' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('translate.google.co.in')

            elif 'open translator' in query:
                jarvis_thought('Opening ...')
                webbrowser.open('translate.google.co.in')

            elif 'open hotstar' in query:
                jarvis_thought('Opening ...')
                webbrowser.open("www.hotstar.com")

            elif 'whats the time now' in query or 'what is the time now' in query:
                strTime = datetime.datetime.now().strftime("%H hour %M minutes=")
                jarvis_thought(f'The time is {strTime}')

            elif 'open console' in query:
                jarvis_thought('Opening ...')
                os.startfile("C:\\Users\\Manbir Singh Judge\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe")

            elif 'open access' in query or 'open ms access' in query:
                jarvis_thought('Opening ...')
                path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
                os.startfile(path)

            elif 'open word' in query or 'open ms word' in query:
                jarvis_thought('Opening ...')
                os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

            elif 'open excel' in query:
                jarvis_thought('Opening ...')
                os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE')

            elif 'open internet explore' in query:
                jarvis_thought('Opening ...')
                os.startfile('C:\\Program Files\\Internet Explorer\\iexplore.exe')

            elif 'open mozilla firefox' in query:
                jarvis_thought('Opening ...')
                os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

            elif 'open firefox' in query:
                jarvis_thought('Opening ...')
                os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

            elif 'open word meaning' in query:
                jarvis_thought('Opening ...')
                os.startfile('D:\\Manbir\\Word meanings.docx')

            elif 'open grammarly' in query:
                jarvis_thought('Opening ...')
                os.startfile('C:\\Users\\Manbir Singh Judge\\AppData\\Local\\GrammarlyForWindows\\GrammarlyForWindows'
                             '.exe')

            elif 'i want to print documents' in query:
                jarvis_thought('Okay, opening HP printer application.')
                os.startfile('C:\\Program Files\\HP\\HP Smart Tank 530 series\\Bin\\HP Smart Tank 530 series.exe')

            elif 'i want to scan documents' in query:
                jarvis_thought('Okay, opening HP scanner application.')
                os.startfile('C:\\Program Files\\HP\\HP Smart Tank 530 series\\Bin\\HP Smart Tank 530 series.exe')

            elif 'i want to change printer setting' in query:
                jarvis_thought('Okay, opening HP printer settings application.')
                os.startfile('C:\\Program Files\\HP\\HP Smart Tank 530 series\\Bin\\HP Smart Tank 530 series.exe')

            elif 'exit' in query:
                jarvis_thought('Bye, see you later.')
                app_running = False

            elif 'bye' in query:
                jarvis_thought('Bye, see you later.')
                app_running = False

            else:
                jarvis_thought('I do not know what to do.')

        if event is None:
            app_running = False

window.close()
sys_exit()
