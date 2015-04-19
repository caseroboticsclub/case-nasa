#! /usr/bin/env python

## file: motor_middleman.py
##
## package: motor_driver 
##
## publishes: revised_motor_velocity_topic
##
## subscribes to: steering_topic
##
## description: send velocity commands from steering node 
## to the profiler

import rospy
from std_msgs.mgs import String
import constants

#steering_topic = "steering_out"
#revised_motor_velocity_topic = "revised_motor_velocity"

to_publish = "motor_middleman"

def on_receive_steering_topic(data):
    to_publish = data

def motor_middleman():
    rospy.init_node('motor_middleman', anonymous=False)
    
    rospy.Subscriber(steering_topic, String, on_receive_steering_topic)

    pub = rospy.Publisher(revised_motor_velocity_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__': 
    try: motor_middleman()
    except rospy.ROSInterruptException: pass

