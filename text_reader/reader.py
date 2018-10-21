__author__ = 'Burik Sergey'
# Чтение вслух
import os
import re
from pygame import mixer
import datetime
import time
from gtts import gTTS

print('Created by Burik Seregey\n you must create file "file.txt" and type there text')


mp3_nameold = '111'
mp3_name = "1.mp3"


mixer.init()

f = open("file.txt", "r")
ss = f.readline()
while ss:
    split_regex = re.compile(r'[.|!|?|…]')
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(ss)])

    for x in sentences:
        if (x != ""):
            print(x)
            tts = gTTS(text=x, lang='ru')
            tts.save(mp3_name)

            mixer.music.load(mp3_name)
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.1)

            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                os.remove(mp3_nameold)
            mp3_nameold = mp3_name

            now_time = datetime.datetime.now()
            mp3_name = now_time.strftime("%d%m%Y%I%M%S") + ".mp3"


    ss = f.readline()


f.close


mixer.music.load('1.mp3')
mixer.stop
mixer.quit


if (os.path.exists(mp3_nameold)):
    os.remove(mp3_nameold)