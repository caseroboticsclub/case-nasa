#! /usr/bin/env python

## file: planner.py
##
## package: planning
##
## publishes: planning_topic
##
## subscribes to: commander_topic
##                slam_topic
##
## description: the main ai code

import rospy
from std_msgs.msg import String
import constants

to_publish = "planner"

def on_receive_commander_topic(data):
    pass

def on_receive_slam_topic(data):
    pass

def planner():
    rospy.init_node('planner', anonymous=False)
    
    rospy.Subscriber(commander_topic, String, on_receive_commander_topic)
    rospy.Subscriber(slam_topic, String, on_receive_slam_topic)
    
    pub = rospy.Publisher(planning_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: planner()
    except rospy.ROSInterruptException: pass
   
