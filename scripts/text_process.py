#!/usr/bin/env python
import re


import rospy, os, sys

from std_msgs.msg import String

rospy.init_node('text_process', anonymous = True)
pub=rospy.Publisher('/Intent',String,queue_size=10)
rate=rospy.Rate(1)

def trigger_response(data):

	response = data.data
	rospy.loginfo("Start to process ::%s",response)
	result=re.search(r"the current state is (?P<state>.+)",response)
	if result:
		state=result.group('state')
		pub.publish(state)
		rate.sleep()

def listener():

	rospy.loginfo("Starting trigger state machine")
	rospy.Subscriber("response",String, trigger_response,queue_size=10)
	rospy.spin()

if __name__ == '__main__':

	listener()
