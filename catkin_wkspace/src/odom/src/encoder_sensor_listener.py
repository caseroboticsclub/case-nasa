#! /usr/bin/env python

## file: encoder_sensor_listener.py
##
## package: odom
##
## publishes: encoder_sensor_data_topic
##
## subscribes to: --
##
## description: interface with motor encoders

import rospy
from std_msgs.mgs import String
import constants

#encoder_sensor_data_topic = "encoder_sensor_data"

# interface with BBB
def BBB():
    return "encoder_sensor_listener"

def encoder():
    rospy.init_node('encoder', anonymous=False)
    
    pub = rospy.Publisher(encoder_sensor_data_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        encoder_data = BBB()
        pub.publish(encoder_data)
        rate.sleep()

if __name__ == '__main__':
    try: encoder()
    except rospy.ROSInterruptException: pass

