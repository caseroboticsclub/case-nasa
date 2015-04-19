#! /usr/bin/env python

## file: soft_estop.py
##
## package: soft_estop
##
## publishes: --
##
## subscribes to: soft_estop_topic
##
## description: shuts down the robot gracefully upon
## receiving soft estop request

import rospy
from stdmsgs.msg import String
import constants

def on_receive_soft_estop_topic(data):
    pass

def soft_estop():
    rospy.init_node('soft_estop', anonymous=False)
    
    rospy.Subscribe(soft_estop_topic, String, on_receive_soft_estop_topic)

    rospy.spin()

if __name__ == '__main__':
    soft_estop()

