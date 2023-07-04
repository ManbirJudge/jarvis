import pyttsx3

# setup
engine = pyttsx3.init('sapi5', True)
voices = engine.getProperty('voices')

engine.setProperty('rate', 145)
engine.setProperty('voice', voices[0].id)


# speak util function
def speak(msg: str):
    engine.say(msg)
    engine.runAndWait()


# main logic
if __name__ == '__main__':
    speak('While the goal is to encapsulate/hide the specific objects and code used by the GUI framework you are '
          'running on top of, if needed you can access the frameworks\' dependent widgets and windows directly. If a '
          'setting or feature is not yet exposed or accessible using the PySimpleGUI APIs, you are not walled off '
          'from the framework. You can expand capabilities without directly modifying the PySimpleGUI package itself.')
