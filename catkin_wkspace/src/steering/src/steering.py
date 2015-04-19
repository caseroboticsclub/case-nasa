#! /usr/bin/env python

## file: steering.py
##
## package: steering
##
## publishes: steering_topic
##
## subscribes to: planning_topic
##                slam_topic
##
## description: corrects velocity commands

import rospy
from stdmsgs.msg import String
import constants

to_publish = "steering"

def on_receive_planning_topic(data):
    pass

def on_receive_slam_topic(data):
    pass

def steering():
    rospy.init_node('steering', anonymous=False)
    
    pub = rospy.Publisher(steering_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(planning_topic, String, on_receive_planning_topic)
    rospy.Subscribe(slam_topic, String, on_receive_slam_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: steering()
    except rospy.ROSInterruptException: pass
  
