#! /usr/bin/env python

## file: encoder_processor.py
##
## package: odom
##
## publishes: encoder_topic
##
## subscribes to: encoder_sensor_data_topic
##                encoder_reset_topic
##
## description: transform encoder data into meaningful info.

import rospy
from stdmsgs.msg import String
import constants

to_publish = ""

def on_receive_encoder_sensor_data_topic(data):
    to_publish = data

def on_receive_encoder_reset_topic(data):
    pass

def encoder_processor():
    rospy.init_node('encoder_processor', anonymous=False)
    
    rospy.Subscriber(encoder_sensor_data_topic, String, on_receive_encoder_sensor_data_topic)
    rospy.Subscriber(encoder_reset_topic, String, on_receive_encoder_reset_topic)

    pub = rospy.Publisher(encoder_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: encoder_processor()
    except rospy.ROSInterruptException: pass
   
