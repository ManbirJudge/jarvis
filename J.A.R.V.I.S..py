from sys import exit as sys_exit
import os
import datetime
from typing import Any

import PySimpleGUI as sg
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

sg.theme("systemDefault")

layout = [
    [sg.Output(size=(50, 15), font='Courier 10')],
    [sg.Button('Take Command', size=(13, 1), key='CMD')]
]

window = sg.Window('J.A.R.V.I.S.', layout=layout, icon='icon.ico')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour <= 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am Jarvis, How can I help you?")


def take_command() -> str | None:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
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


def log(msg: Any, type_: str):
    if type_ == 'err':
        print(f'[_ERROR_] {msg}')


if __name__ == '__main__':
    i = 1

    while True:
        if i == 1:
            greet()
            i += 1

        event, value = window.read()

        if event == 'CMD':
            query = take_command().lower()

            if 'hello jarves' in query:
                print("Jarvis:", "Hello")
                speak("Hello")

            elif 'hello jarvis' in query:
                print("Jarvis:", "Hello")
                speak("Hello")

            elif 'hello' in query:
                print("Jarvis:", "Hello")
                speak("Hello")

            elif 'how are you' in query:
                print("Jarvis: I am fine. How are you?")
                speak("I am fine. How are you?")

            elif 'i am fine' in query:
                print("Jarvis: Ok-ok, but now please give me a command.")
                speak("ok-ok, but now please give me a command.")

            elif 'i am also fine' in query:
                print("Jarvis: Ok-ok, but now please give me a command")
                speak("ok-ok, but now please give me a command")

            elif 'open google chrome' in query:
                print('Jarvis:', 'Okay, Opening Google.')
                speak('Okay, Opening Google')

                try:
                    path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(path)

                except:
                    print('Jarvis:', 'Cannot Find Google Chrome is your System')
                    speak('Cannot Find Google Chrome is your System')

            elif 'according to wikipedia' in query:
                print("Jarvis: I am searching on wikipedia...")
                speak("I am searching on wikipedia...")
                query = query.replace('according to wikipedia', '')
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(result)
                speak(result)

            elif 'open youtube' in query:
                print("Jarvis: Okay")
                speak("Okay")
                webbrowser.open('youtube.com')

            elif 'open google maps' in query:
                print("Jarvis: Okay")
                speak("Okay")
                webbrowser.open('maps.google.com')

            elif 'open gmail' in query:
                print("Jarvis: Okay")
                speak("Okay")
                webbrowser.open('gmail.com')

            elif 'open google docs' in query:
                print("Jarvis: Okay")
                speak("Okay")

                webbrowser.open('docs.google.com')

            elif 'open google sheets' in query:
                print("Jarvis: Okay")
                speak("Okay")

                webbrowser.open('sheets.google.com')

            elif 'open google slides' in query:
                print("Jarvis: Okay")
                speak("Okay")

                webbrowser.open('slides.google.com')

            elif 'open tribune epaper' in query:
                print('Jarvis:', 'Okay')
                speak('Okay')

                webbrowser.open('epaper.tribuneindia.com')

            elif 'open translator' in query:
                print('Jarvis:', 'Okay')
                speak('Okay')

                webbrowser.open('translate.google.co.in')

            elif 'open hotstar' in query:
                print('Jarvis:', 'Okay')
                speak("OKay")
                webbrowser.open("www.hotstar.com/in")

            elif 'whats the time now' in query or 'what is the time now' in query:
                strTime = datetime.datetime.now().strftime("%H hour %M minutes=")
                print("The time is:", strTime)
                speak("The time is " + strTime)

            elif 'open console window' in query:
                print("Jarvis: Okay")
                speak("Okay")
                os.startfile("C:\\Users\\Manbir Singh Judge\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe")

            elif 'open access' in query or 'open ms access' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
                os.startfile(path)

            elif 'open word' in query or 'open ms word' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(path)

            elif 'open excel' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(path)

            elif 'open internet explore' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
                os.startfile(path)

            elif 'open mozilla firefox' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(path)

            elif 'open firefox' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(path)

            elif 'open word meaning' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "D:\\Manbir\\Word meanings.docx"
                os.startfile(path)

            elif 'open grammarly' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Users\\Manbir Singh Judge\\AppData\\Local\\GrammarlyForWindows\\GrammarlyForWindows.exe"
                os.startfile(path)

            elif 'open grammarly editor' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Users\\Manbir Singh Judge\\AppData\\Local\\GrammarlyForWindows\\GrammarlyForWindows.exe"
                os.startfile(path)

            elif 'do you have a cup of tea' in query:
                print("Sorry, I can not drink  tea.")
                speak("Sorry, I can not drink  tea.")

            elif 'do you have a cup of coffee' in query:
                print("Sorry, I can not drink  coffee.")
                speak("Sorry, I can not drink coffee.")

            elif 'do you have a glass of water' in query:
                print("Sorry, I can not drink  water.")
                speak("Sorry, I can not drink water.")

            elif 'i want to print documents' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files\\HP\\HP Smart Tank 530 series\\Bin\\HP Smart Tank 530 series.exe"
                os.startfile(path)

            elif 'i want to scan documents' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files\\HP\\HP Smart Tank 530 series\\Bin\\HP Smart Tank 530 series.exe"
                os.startfile(path)

            elif 'i want to change printer setting' in query:
                print("Jarvis: Okay")
                speak("Okay")
                path = "C:\\Program Files\\HP\\HP Smart Tank 530 series\\Bin\\HP Smart Tank 530 series.exe"
                os.startfile(path)

            elif 'exit' in query:
                print("bye, see you later")
                speak("bye, see you later")
                break

            elif 'bye-bye' in query:
                print("bye, see you later")
                speak("bye, see you later")
                break

        if event is None:
            break

window.close()
sys_exit()
