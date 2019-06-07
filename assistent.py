import os 
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

#options
opts = {
	"alias" : ("jeff", "josh", "jess", "jeffi"),
	"tbr" : ("tell", "show", "how much", "say"),
	"cmds": {
        "ctime": ('current time','what time is it now'),
        "radio": ('turn on the music','switch on the music','turn on the radio'),
        "stupid1": ('tell a joke','make me laugh.я','you know jokes')
    }

}

# functions
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
 
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] recognized: " + voice)
   
        if voice.startswith(opts["alias"]):
         
            cmd = voice
 
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
           
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
           
            # recognize and execute the command
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        print("[log] voice not recognized!")
    except sr.RequestError as e:
        print("[log] Unknown Error, please, check your internet!")
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
   
    return RC
 
def execute_cmd(cmd):
    if cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        speak("current time is " + str(now.hour) + ":" + str(now.minute))
   
    elif cmd == 'radio':
        # play radio
        os.system("D:\\Jarvis\\res\\radio_record.m3u")
   
    elif cmd == 'stupid1':
        # joke
        speak("it is a very good joke.....")
   
    else:
        print("l can't understand you, please repeat!")

# start
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
    r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()
 