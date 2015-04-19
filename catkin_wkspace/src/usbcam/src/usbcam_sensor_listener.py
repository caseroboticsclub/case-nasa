#! /usr/bin/env python

## file: usbcam_sensor_listener.py
##
## package: usbcam
##
## publishes: usbcam_sensor_data_topic
##
## subscribes to: --
##
## description: interfaces with usbcam(s)

import rospy
from stdmsgs.msg import String
import constants

def BBB():
    return "usbcam_sensor_listener"

def usbcam_sensor_listener():
    rospy.init_node('usbcam_sensor_listener', anonymous=True)
    
    pub = rospy.Publisher(usbcam_sensor_data_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        to_publish = BBB()
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: usbcam_sensor_listener()
    except rospy.ROSInterruptException: pass
  
