#! /usr/bin/env python

## file: load_cell_sensor_listener.py
##
## package: load_cell
##
## publishes: load_cell_sensor_data_topic
##
## subscribes to: --
##
## description: interfaces with load_cell sensor(s)

import rospy
from stdmsgs.msg import String
import constants

def BBB():
    return "load_cell_sensor_listener"

def load_cell_sensor_listener():
    rospy.init_node('load_cell_sensor_listener', anonymous=True)
    
    pub = rospy.Publisher(load_cell_sensor_data_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        to_publish = BBB()
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: load_cell_sensor_listener()
    except rospy.ROSInterruptException: pass
  
