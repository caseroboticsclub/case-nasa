#! /usr/bin/env python

## file: usbcam_processor.py
##
## package: usbcam
##
## publishes: usbcam_topic
##
## subscribes to: usbcam_sensor_data_topic
##
## description: transforms usbcam data into meaningful info.

import rospy
from stdmsgs.msg import String
import constants

to_publish = "usbcam_processor"

def on_receive_usbcam_sensor_data_topic(data):
    to_publish = data

def usbcam_sensor_listener():
    rospy.init_node('usbcam_processor', anonymous=False)
    
    pub = rospy.Publisher(usbcam_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(usbcam_sensor_data_topic, String, on_receive_usbcam_sensor_data_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: usbcam_processor()
    except rospy.ROSInterruptException: pass
  
