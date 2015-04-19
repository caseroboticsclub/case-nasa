#! /usr/bin/env python

## file: odom.py
##
## package: odom
##
## publishes: odometry_topic
##            encoder_reset_topic
##
## subscribes to: encoder_topic
##
## description: performs cumulative odometry using data from 
## encoder_processor

import rospy
from std_msgs.msg import String
import constants

#odometry_topic = "odometry_state_estimation"
#encoder_reset_topic = "encoder_reset"
#encoder_topic = "encoder_data_processed"

state_to_publish = ""
reset_to_publish = ""
reset = False

def on_receive_encoder_topic(data):
    to_publish = data

def odom():
    rospy.init_node('odom', anonymous=False)
    
    rospy.Subscriber(encoder_topic, String, on_receive_encoder_data)
    pub_state = rospy.Publisher(odometry_topic, String, queue_size=10)
    pub_reset = rospy.Publisher(encoder_reset_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pub_state.publish(state_to_publish)
        if(reset):
            pub_reset.publish(reset_to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: odom()
    except rospy.ROSInterruptException: pass

