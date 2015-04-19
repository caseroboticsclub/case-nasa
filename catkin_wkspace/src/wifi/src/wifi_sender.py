#! /usr/bin/env python

## file: wifi_sender.py
##
## package: wifi
##
## publishes: wifi_topic
##
## subscribes to: user_input_topic
##
## description: senders user commands over wifi

import rospy
from std_msgs.msg import String
import constants

to_publish = "wifi_sender"

def on_receive_user_input_topic(data):
    to_publish = data

def wifi_sender():
    rospy.init_node('wifi_sender', anonymous=False)
    
    pub = rospy.Publisher(wifi_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(user_input_topic, String, on_receive_user_input_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: wifi_sender()
    except rospy.ROSInterruptException: pass
  
