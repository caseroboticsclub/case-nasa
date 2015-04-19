#! /usr/bin/env python

## file: actuator_processor.py
##
## package: actuator
##
## publishes: actuator_topic
##
## subscribes to: actuator_sensor_data_topic
##
## description: converts actuator sensor data to meaningful form

import rospy
from stdmsgs.msg import String
import constants

to_publish = "actuator_processor"

def on_receive_actuator_sensor_data_topic(data);
    to_publish = data

def actuator_processor():
    
    rospy.init_node('actuator_processor', anonymous=False)

    pub = rospy.Publisher(actuator_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(actuator_sensor_data_topic, String, on_receive_actuator_sensor_data_topic)
    
    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: actuator_processor()
    except rospy.ROSInterruptException: pass

