#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import rospy
import aiml
import os
import sys

from gtts import gTTS
from pygame import mixer
import tempfile

from std_msgs.msg import String

rospy.init_node('aiml_server')
mybot = aiml.Kernel()
response_publisher = rospy.Publisher('response',String,queue_size=10)


def is_chinese(uchar):
	if uchar >u'\u4e00' and uchar<=u'\u9fa5' :
		return True
	else:
		return False



def load_aiml(xml_file):

	data_path = rospy.get_param("aiml_path")
	#data_path="/home/shannon/Documents/ros-kinetic/src/ros_aiml/data"
	print data_path
	os.chdir(data_path)


	if os.path.isfile("standard.brn"):
		mybot.bootstrap(brainFile = "standard.brn")

	else:
		mybot.bootstrap(learnFiles = xml_file, commands = "load aiml b")
		mybot.saveBrain("standard.brn")

def speak(sentence):
	with tempfile.NamedTemporaryFile(delete=True) as fp:
		tts=gTTS(text=sentence,lang='zh-tw')
		tts.save("{}.mp3".format(fp.name))
		mixer.init()
		mixer.music.load('{}.mp3'.format(fp.name))
		mixer.music.play(1)


def callback(data):

	input = data.data
	response = mybot.respond(input)
	rospy.loginfo("I heard:: %s",data.data)
	rospy.loginfo("I spoke:: %s",response)
	#rospy.loginfo("I spoke:: %s",response.decode('utf-8'))
	#print("hahaha",response.decode('utf-8'))
	response_publisher.publish(response)
	if is_chinese(response.decode('utf-8'))==True:
		print("chinese")
		speak(response.decode('utf-8'))




def listener():

	rospy.loginfo("Starting ROS AIML Server")
	rospy.Subscriber("chatter", String, callback)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':

	load_aiml('startup.xml')
	listener()
