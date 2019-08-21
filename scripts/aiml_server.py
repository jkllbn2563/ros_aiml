#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import rospy
import aiml
import os
import sys
import re
from gtts import gTTS
from pygame import mixer
import tempfile
import warnings
from std_msgs.msg import String
import time
warnings.filterwarnings("ignore")

rospy.init_node('aiml_server')
mybot = aiml.Kernel()
response_publisher = rospy.Publisher('response',String,queue_size=10)
pub=rospy.Publisher('/Intent',String,queue_size=10)

rate=rospy.Rate(1)
localtime=time.asctime(time.localtime(time.time()))

def is_chinese(uchar):
	if uchar >u'\u4e00' and uchar<=u'\u9fa5' :
		return True
	else:
		return False



def load_aiml(xml_file):

	#data_path = rospy.get_param("aiml_path")
	data_path="/home/jkllbn2563/catkin_ws/src/ros_aiml/data"
	print data_path
	os.chdir(data_path)


	if os.path.isfile("standard.brn"):
		mybot.bootstrap(brainFile = "standard.brn")

	else:
		mybot.bootstrap(learnFiles = xml_file, commands = "load aiml b")
		mybot.saveBrain("standard.brn")


def callback(data):

	input = data.data
	response = mybot.respond(input)
	#rospy.loginfo("I heard:: %s",data.data)
	#rospy.loginfo("I spoke:: %s",response)
	#rospy.loginfo("I spoke:: %s",response.decode('utf-8'))
	#print("hahaha",response.decode('utf-8'))
	rospy.loginfo("Start to process ::%s",response)
	result=re.search(r"the current state is (?P<state>.+)",response)
	time_result=re.search(r"now the time is",response)

	if result:
		state=result.group('state')
		pub.publish(state)
		rate.sleep()

	if time_result:
		state=localtime
		state=str(state[11:13])+" o'clock and "+str(state[14:16])+" minutes"
		response=re.sub(r"Friday","",response)
		response=response+state



	response=re.sub(r",and the current state is (?P<state>.+)","",response)

	

	rospy.loginfo("I heard:: %s",data.data)

	rospy.loginfo("I spoke process:: %s",response)

	response_publisher.publish(response)
	#response_publisher.publish(response_time)

	

	




def listener():

	rospy.loginfo("Starting ROS AIML Server")
	rospy.Subscriber("chatter", String, callback)
    
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':


  
	load_aiml('startup.xml')
	listener()
