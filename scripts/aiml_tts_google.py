#!/usr/bin/env python
import rospy, os, sys
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
import re
from gtts import gTTS
from pygame import mixer
from std_msgs.msg import String
import tempfile
rospy.init_node('google_tts_bridge', anonymous = False)

soundhandle = SoundClient()
rospy.sleep(1)
soundhandle.stopAll()
print 'Starting TTS'

def speak(sentence):
	with tempfile.NamedTemporaryFile(delete=True) as fp:
		tts=gTTS(text=sentence,lang='zh-tw')
		tts.save("{}.mp3".format(fp.name))
		mixer.init()
		mixer.music.load('{}.mp3'.format(fp.name))
		mixer.music.play(1)
def speak_english(sentence):
	with tempfile.NamedTemporaryFile(delete=True) as fp:
		tts=gTTS(text=sentence,lang='en-us')
		tts.save("{}.mp3".format(fp.name))
		mixer.init()
		mixer.music.load('{}.mp3'.format(fp.name))
		mixer.music.play(1)



def is_chinese(uchar):
	if uchar >u'\u4e00' and uchar<=u'\u9fa5' :
		return True
	else:
		return False

def get_response(data):

	response = data.data
	rospy.loginfo("Response ::%s",response)
	#local tts
	#if is_chinese(response)==False:
		#soundhandle.say(response)

	if is_chinese(response.decode('utf-8'))==True:
		print("Now the language is chinese")
		speak(response.decode('utf-8'))

	else :
		print("Now the language is english")
		speak_english(response)


def listener():

	rospy.loginfo("Starting listening to response")
	rospy.Subscriber("response",String, get_response,queue_size=10)
	rospy.spin()


if __name__ == '__main__':

	listener()
