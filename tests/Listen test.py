import speech_recognition as sr

# setup
recognizer = sr.Recognizer()

recognizer.pause_threshold = 1

# getting audio from microphone
print('Listening ...')
with sr.Microphone() as source:
    audio = recognizer.listen(source)

# recognizing
print('Recognizing ...')

try:
    text = recognizer.recognize_google(audio, language='en-in')
    print(f'\nYou probably said:\n{text}')
except Exception as e:
    print(e)
