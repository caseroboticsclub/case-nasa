#! /usr/bin/env python

## file: wifi_receiver.py
##
## package: wifi
##
## publishes: user_commands_topic
##
## subscribes to: wifi_topic
##
## description: receivers user commands over wifi

import rospy
from std_msgs.msg import String
import constants

to_publish = "wifi_receiver"

def on_receive_wifi_topic(data):
    to_publish = data

def wifi_receiver():
    rospy.init_node('wifi_receiver', anonymous=False)
    
    pub = rospy.Publisher(user_commands_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(wifi_topic, String, on_receive_wifi_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: wifi_receiver()
    except rospy.ROSInterruptException: pass
  
