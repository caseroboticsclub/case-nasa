#! /usr/bin/env python

## file: kinect_sensor_listener.py
##
## package: kinect
##
## publishes: kinect_sensor_data_topic
##
## subscribes to: --
##
## description: interfaces with kinect sensor

import rospy
from std_msgs.mgs import String
import constants

#kinect_sensor_data_topic = "kinect_sensor_data"

def BBB():
    return "kinect_sensor_listener"

def kinect_sensor_listener():
    rospy.init_node('kinect_sensor_listener', anonymous=False)
    
    pub = rospy.Publisher(kinect_sensor_data_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        to_publish = BBB();
        rospy.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: kinect_sensor_listener()
    except rospy.ROSInterruptException: pass

