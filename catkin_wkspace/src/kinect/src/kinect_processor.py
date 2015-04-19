#! /usr/bin/env python

## file: kinect_processor.py
##
## package: kinect
##
## publishes: kinect_topic
##
## subscribes to: kinect_sensor_data_topic
##
## description: transforms kinect sensor data into meaningful 
## information

import rospy
from std_msgs.mgs import String
import constants

#kinect_sensor_data_topic = "kinect_sensor_data"

to_publish = "kinect_processor"

def on_receive_kinect_sensor_data_topic(data):
    to_publish = data

def kinect_processor():
    rospy.init_node('kinect_processor', anonymous=False)
    
    rospy.Subscriber(kinect_sensor_data_topic, String, on_receive_kinect_sensor_data_topic)
    
    while not rospy.is_shutdown():
        rospy.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: kinect_processor()
    except rospy.ROSInterruptException: pass
 
