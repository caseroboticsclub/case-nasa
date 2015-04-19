#! /usr/bin/env python

## file: power_analyzer.py
##
## package: power
##
## publishes: power_topic
##
## subscribes to: current_sensor_data_topic
##                current_sense_sensor_data_topic
##
## description: interfaces with current sensor

import rospy
from std_msgs.msg import String
import constants

to_publish = "power_analyzer"

def on_receive_current_sensor_data_topic(data):
    pass

def on_receive_current_sense_sensor_data_topic(data):
    pass    

def power_analyzer():
    rospy.init_node('power_analyzer', anonymous=False)
    
    pub = rospy.Publisher(power_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(current_sensor_data_topic, String, on_receive_current_sensor_data_topic)

    rospy.Subscribe(current_sense_sensor_data_topic, String, on_receive_current_sense_sensor_data_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: power_analyzer()
    except rospy.ROSInterruptException: pass
   
