#! /usr/bin/env python

## file: motor_velocity_profiler.py
##
## package: velocity_profiling
##
## publishes: profiled_motor_velocity_topic
##
## subscribes to: revised_motor_velocity_topic
##
## description: corrects velocity commands

import rospy
from std_msgs.msg import String
import constants

to_publish = "motor_velocity_profiler"

def on_receive_revised_motor_velocity_topic(data):
    to_publish = data   

def motor_velocity_profiler():
    rospy.init_node('motor_velocity_profiler', anonymous=False)
    
    pub = rospy.Publisher(profiled_motor_velocity_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscribe(revised_motor_velocity_topic, String, on_receive_revised_motor_velocity_topic)

    while not rospy.is_shutdown():
        pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: motor_velocity_profiler()
    except rospy.ROSInterruptException: pass
  
