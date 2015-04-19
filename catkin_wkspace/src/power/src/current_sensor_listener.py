#! /usr/bin/env python

## file: current_sensor_listener.py
##
## package: power
##
## publishes: current_sensor_data_topic
##
## subscribes to: --
##
## description: interfaces with current sensor

import rospy
from std_msgs.msg import String
import constants

def BBB():
    return "current_sensor_listener"

def current_sense_sensor_listener():
    rospy.init_node('current_sensor_listener', anonymous=False)
    
    pub = rospy.Publisher(current_sensor_data_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        to_publish = BBB()
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: current_sensor_listener()
    except rospy.ROSInterruptException: pass
   
