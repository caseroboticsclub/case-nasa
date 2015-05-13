#! /usr/bin/env python

'''
file: saber_sender_arduino.py
package: saber_sender
publishes: --
subscribes to: saber_sender_topic (type: int64[3])
'''

import rospy
from constants.src import constants

addr = ''
opt = ''
data = []

def on_receive_saber_sender_topic(message):
    global addr
    global opt
    global data
    str(message[0]) = addr
    str(message[1]) = opt
    int_data = message[2]
    data = to_bytes(int_data)

def saber_sender_arduino():
    rospy.init_node('saber_sender_arduino')
    rospy.Subscribe(saber_sender_topic, int64[], anonymous=False)

    rospy.spin()

def to_bytes(int_data):
    byte_array = [0,0]
    if int_data > 255:
        byte_array[0] = int_data - 255
    byte_array[1] = int_data % 256 
    return byte_array

