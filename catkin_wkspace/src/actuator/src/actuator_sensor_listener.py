#! /usr/bin/env python

## file: actuator_sensor_listener.py
##
## package: actuator
##
## publishes: actuator_sensor_data_topic
##
## subscribes to: -- 
##
## description: interfaces with Hall Effect sensors on actuator

import rospy
from std_msgs.msg import String
import constants

#actuator_sensor_data_topic = "actuator_sensor_data"

def BBB():
    return "actuator_sensor_listener"

def actuator_sensor_listener():
    
    rospy.init_node('actuator_sensor_listener', anonymous=False)
    pub = rospy.Publisher(actuator_sensor_data_topic, String, queue_size=10)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        to_publish = BBB();
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: actuator_sensor_listener()
    except rospy.ROSInterruptException: pass
