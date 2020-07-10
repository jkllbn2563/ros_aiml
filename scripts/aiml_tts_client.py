#!/usr/bin/env python

import speech_recognition

import rospy, os, sys
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
import re
from gtts import gTTS
from pygame import mixer
from std_msgs.msg import String
import tempfile
from std_srvs.srv import Trigger, TriggerResponse
from std_msgs.msg import String
rospy.init_node('aiml_soundplay_client', anonymous = True)
r=speech_recognition.Recognizer()
soundhandle = SoundClient()
#rospy.sleep(1)
soundhandle.stopAll()
pub=rospy.Publisher('/chatter',String,queue_size=10)

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

def executeVoice(req):
	with speech_recognition.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=0.5)
		audio=r.record(source,duration=4)
		
		print("You said for service " + r.recognize_google(audio,language='en-US'))
		pub.publish(r.recognize_google(audio,language='en-US'))
		keywords=["station A","station B","follow","home","repository","happened"]
		for i in keywords:
			if re.findall(i,r.recognize_google(audio,language='en-US'),flags=re.IGNORECASE):
				return TriggerResponse(
        success=True,
        message=r.recognize_google(audio,language='en-US'))


	return TriggerResponse(
        success=False,
        message=r.recognize_google(audio,language='en-US')
    )

#def say(text):
    #pygame.init()
    #tts = gTTS(text=text, lang='en')
    #fp = BytesIO()
    #tts.write_to_fp(fp)
    #fp.seek(0)
    #mixer.init()
    #mixer.music.load(fp)
    #mixer.music.play()
    #while mixer.music.get_busy():
        #pygame.time.Clock().tick(10)

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
		try:
			print("Now the language is chinese")
			speak(response.decode('utf-8'))
		except:
			print("changing state")

	else :
		try:
			print("Now the language is english")
			speak_english(response)
			#say(response)
		except:
			print("changing state")


def listener():

	rospy.loginfo("Starting listening to response")
	rospy.Subscriber("response",String, get_response,queue_size=10)
	rospy.spin()


if __name__ == '__main__':
	s=rospy.Service("golden_voice",Trigger,executeVoice)
	rospy.wait_for_service('/golden_voice')

	# create triggerCaption server for main state machine trigger
	triggerVoice_server=rospy.ServiceProxy('/golden_voice',Trigger)
	listener()
		   
