#!/usr/bin/env python
#-*- coding: utf-8 -*-
from gtts import gTTS
from pygame import mixer
import tempfile
import sys
import rospy
from std_msgs.msg import String

sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
sys.path.append("/opt/ros/kinetic/share")





def speak(sentence):
	with tempfile.NamedTemporaryFile(delete=True) as fp:
		tts=gTTS(text=sentence,lang='zh-tw')
		tts.save('{}.mp3'.format(fp.name))
		mixer.init()

		mixer.music.load('{}.mp3'.format(fp.name))
		mixer.music.play()


speak('我好帥')