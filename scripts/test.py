#!/usr/bin/env python
#-*- coding: utf-8 -*-
from gtts import gTTS
import tempfile
from pygame import mixer
import sys
 

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang='zh-tw')
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(2)
speak(u'\u6211\u77e5\u9053')
print("hahahha")
