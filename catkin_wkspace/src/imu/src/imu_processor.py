#! /usr/bin/env python

## file: imu_processor.py
##
## package: imu
##
## publishes: imu_topic
##
## subscribes to: imu_sensor_data_topic
##
## description: transforms imu sensor data to meaningful form

import rospy
from stdmsgs.msg import String
import constants

to_publish = "imu_processor"

def on_receive_imu_sensor_data_topic(data):
    to_publish = data

def imu_processor():
    rospy.init_node('imu_processor', anonymous=False)
    
    pub = rospy.Publisher(imu_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(imu_sensor_data_topic, String, on_receive_imu_sensor_data_topic)
    
    while not rospy.is_shutdown():
        rospy.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: imu_processor()
    except rospy.ROSInterruptException: pass
   
