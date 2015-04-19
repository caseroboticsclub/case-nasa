#! /usr/bin/env python

## file: commander.py
##
## package: commander 
##
## publishes: commander_topic
##
## subscribes to: user_commands_topic
##
## description: delivers high-level commands to robot and 
## listens to user input if applicable

import rospy
from std_msgs.msg import String
import constants

#user_commands_topic = "user_commands_received"
#commander_topic = "high_commands"

to_publish = "commander"

def on_receive_user_commands_topic(data):
    to_publish = data

def commander():
    
    rospy.init_node('commander', anonymous=True)
    
    pub = rospy.Publisher(commander_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscriber(user_commands_topic, String, on_receive_user_commands_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: commander()
    except rospy.ROSInterruptException: pass
