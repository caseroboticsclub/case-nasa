#! /usr/bin/env python

## file: imu_sensor_listener.py
##
## package: imu
##
## publishes: imu_sensor_data_topic
##
## subscribes to: --
##
## description: interfaces with the imu sensor

import rospy
from std_msgs.mgs import String
import constants

#imu_sensor_topic = "imu_sensor_data"

def BBB():
    return "imu_sensor_listener"

def imu_sensor_listener():
    rospy.init_node('imu_sensor_listener', anonymous=True)
    
    pub = rospy.Publisher(imu_sensor_data_topic, String, queue_size=10)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        to_publish = BBB();
        rospy.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: imu_sensor_listener()
    except rospy.ROSInterruptException: pass

