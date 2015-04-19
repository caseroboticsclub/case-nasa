#! /usr/bin/env python

## file: ui.py
##
## package: ui
##
## publishes: user_input_topic
##
## subscribes to: --
##
## description: harvests user input and sends it along
## its merry way.

import rospy
from stdmsgs.msg import String
import constants

def STDIN():
    return "ui"

def ui():
    rospy.init_node('ui', anonymous=False)
    
    pub = rospy.Publisher(user_input_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        to_publish = STDIN()
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: ui()
    except rospy.ROSInterruptException: pass
  
