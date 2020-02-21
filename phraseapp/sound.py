# pip install pyttsx3 pypiwin32
import pyttsx3

# One time initialization
engine = pyttsx3.init()

# Set properties _before_ you add things to say
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Queue up things to say.
# There will be a short break between each one
# when spoken, like a pause between sentences.
def pronounce(text, *args):
    print(text)
    engine.say(text)
    engine.runAndWait()


