#!/usr/bin/env python
#-*- coding: utf-8 -*-
import speech_recognition
import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
sys.path.append("/opt/ros/kinetic/share")
import rospy
from std_msgs.msg import String
#from pynupt.keyboard import Key,controller
import keyboard
import warnings

warnings.filterwarnings("ignore")

#keyboard.press_and_release('shift+s, space')
r=speech_recognition.Recognizer()
#keyboard=Controller()

pub=rospy.Publisher('/chatter',String,queue_size=10)
rospy.init_node('google_api',anonymous=True)
rate=rospy.Rate(1)
#device_index=0
def listen():
	with speech_recognition.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=0.5)
		audio=r.record(source,duration=4)
		#audio=r.listen(source)
		#print("You said " + r.recognize_google(audio,language='zh-TW'))
		print("You said " + r.recognize_google(audio,language='en-US'))

		#r.recognize_google(audio,language='en-US')
		#pub.publish(r.recognize_google(audio,language='zh-TW').encode('utf-8'))
		pub.publish(r.recognize_google(audio,language='en-US'))

		rate.sleep()
		



		


while not rospy.is_shutdown():
	
	#print("press enter to start")
	#keyboard.wait('enter')
	raw_input()
	try:
		

			listen()
			
			#if keyboard.is_press('s'):
				#print("start to analyze...")
				#break
			#else:
				#pass




		
		#print("You said " + r.recognize_google(audio,language='zh-TW'))
			#print( r.recognize_google(audio,language='en-US'))

		
		   	#pub.publish(r.recognize_google(audio,language='zh-TW').decode('unicode-escape'))
		   	


	except:                            
		  print("Could not understand audio")


