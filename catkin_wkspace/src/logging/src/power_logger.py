#! /usr/bin/env python

## file: power_logger.py
##
## package: logging
##
## publishes: --
##
## subscribes to: power_topic
##                commander_topic
##
## description: logs power usage

import rospy
from std_msgs.msg import String
import constants

def on_receive_power_topic(data):
    pass

def on_receive_commander_topic(data):
    pass

def power_logger():
    rospy.init_node('power_logger', anonymous=False)
    
    rospy.Subscribe(power_topic, String, on_receive_power_topic)

    rospy.Subscribe(commander_topic, String, on_receive_commander_topic)

    rospy.spin()

if __name__ == '__main__':
    power_logger()
   
