#! /usr/bin/env python

## file: dig.py
##
## package: dig
##
## publishes: --
##
## subscribes to: commander_topic
##
## description: interfaces with the digging wheel. delivers
## simple on/off, forward/reverse toggle commands

import rospy
from std_msgs.msg import String
import constants

#commander_topic = "high_commands"

def on_receive_commander_topic(data):
    # send toggle command to saber controlling dig wheel
    # (use module in motor_driver package for serial)
    pass

def dig():
    rospy.init_node('dig', anonymous=False)
    rospy.Subscriber(commander_topic, String, on_receive_commander_topic)
    
    rospy.spin()

if __name__ == '__main__': 
    dig()
