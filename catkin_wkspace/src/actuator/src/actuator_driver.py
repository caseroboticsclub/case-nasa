#! /usr/bin/env python

## file: actuator_driver.py
##
## publishes: desired_position_topic
##            (interfaces with physical device)
##
## subscribes to: commander_topic
##                steering_topic
##
## description: middleman betweent the actuators and the 
## high-level commands, similar to motor_middleman

import rospy
from std_msgs.msg import String
import constants

#desired_position_topic = "desired_position_actuator"
#commander_topic = "high_commands"
#steering_topic = "steering_commands_out"

def on_receive_commander_topic(command):
    print('received '+command) 

def on_receive_steering_topic(command):
    print('received '+command)

def actuator_driver():
    
    rospy.init_node('actuator_driver', anonymous=False)
    
    rospy.Subscriber(commander_topic, String, on_receive_commander_topic)
    rospy.Subscriber(steering_topic, String, on_receive_steering_topic)

    pub = rospy.Publisher(desired_position_topic, String, queue_size=10)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        pub.publish("actuator_driver to steering: do you read?")
        rate.sleep()

if __name__ == '__main__':
    try: actuator_driver()
    except rospy.ROSInterruptException: pass
