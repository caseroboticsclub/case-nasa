#! /usr/bin/env python

## file: power_err.py
##
## package: power
##
## publishes: soft_estop_topic
##
## subscribes to: power_topic
##
## description: monitors power usage

import rospy
from std_msgs.msg import String
import constants

to_publish = "power_err"
is_err = False

def on_receive_power_topic(data):
    pass

def power_err():
    rospy.init_node('power_err', anonymous=False)
    
    pub = rospy.Publisher(soft_estop_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(power_topic, String, on_receive_power_topic)

    while not rospy.is_shutdown():
        if(is_err):
            pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: power_err()
    except rospy.ROSInterruptException: pass
   
