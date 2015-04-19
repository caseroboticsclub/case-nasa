#! /usr/bin/env python

## file: slam.py
##
## package: slam
##
## publishes: slam_topic
##
## subscribes to: actuator_topic
##                imu_topic
##                kinect_topic
##                usbcam_topic
##                odometry_topic
##
## description: simultaneous localization and mapping

import rospy
from stdmsgs.msg import String
import constants

to_publish = "slam"

def on_receive_actuator_topic(data):
    pass

def on_receive_imu_topic(data):
    pass

def on_receive_kinect_topic(data):
    pass

def on_receive_usbcam_topic(data):
    pass

def on_receive_odometry_topic(data):
    pass

def slam():
    rospy.init_node('slam', anonymous=False)
    
    pub = rospy.Publisher(slam_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(actuator_topic, String, on_receive_actuator_topic)
    rospy.Subscribe(imu_topic, String, on_receive_imu_topic)
    rospy.Subscribe(kinect_topic, String, on_receive_kinect_topic)
    rospy.Subscribe(usbcam_topic, String, on_receive_usbcam_topic)
    rospy.Subscribe(odometry_topic, String, on_receive_odometry_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: slam()
    except rospy.ROSInterruptException: pass
   
