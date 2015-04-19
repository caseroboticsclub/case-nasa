#! /usr/bin/env python

## file: load_cell_processor.py
##
## package: load_cell
##
## publishes: load_cell_topic
##
## subscribes to: load_cell_sensor_data_topic
##
## description: transforms load cell sensor data into meaningful info

import rospy
from stdmsgs.msg import String
import constants

to_publish = "load_cell_processor"

def on_receive_load_cell_sensor_data_topic(data):
    to_publish = data

def load_cell_processor():
    rospy.init_node('load_cell_processor', anonymous=False)
    
    pub = rospy.Publisher(load_cell_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(load_cell_sensor_data_topic, String, on_receive_load_cell_sensor_data_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: load_cell_processor()
    except rospy.ROSInterruptException: pass
  
