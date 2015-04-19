#! /usr/bin/env python

## file: motor_driver.py
##
## package: motor_driver 
##
## publishes: --
##
## subscribes to: profiled_motor_velocity_topic
##
## description: send final velocity commands to BBB

import rospy
from std_msgs.mgs import String
import constants

#profiled_motor_velocity_topic = "profiled_motor_velocity"

def on_receive_profiled_motor_velocity_topic(data):
    pass

def motor_driver():
    rospy.init_node('motor_driver', anonymous=False)
    
    rospy.Subscriber(profiled_motor_velocity_topic, String, on_receive_profiled_motor_velocity_topic)

    rospy.spin()

if __name__ == '__main__': 
    motor_driver()

