#! /usr/bin/env python

## file: actuator_err.py
##
## package: actuator
##
## publishes: soft_estop_topic
##
## subscribes to: actuator_topic
##
## description: monitors processed data published by 
## actuator_processor and sends error signal if this value 
## surpasses an upper or lower safe threshold

import rospy
from std_msgs.msg import String
import constants

#soft_stop_topic = "soft_estop"
#actuator_topic = "actuator_data_processed"
#upper_limit = 1
#lower_limit = -1

is_err = False
to_publish = "actuator_err"

def on_receive_actuator_topic(data):
    is_err = False
    to_publish = data

def actuator_err():

    rospy.init_node('actuator_err', anonymous=False)
    
    pub = rospy.Publisher(soft_estop_topic, String, queue_size=10)
    rate = rospy.Rate(10)
    
    rospy.Subscriber(actuator_topic, String, on_receive_actuator_topic)

    while not rospy.is_shutdown():
        if(is_err):        
            pub.publish(to_publish)
        rate.sleep()

if __name__ == '__main__':
    try: actuator_err()
    except rospy.ROSInterruptException: pass
