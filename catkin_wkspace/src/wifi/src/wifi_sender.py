#! /usr/bin/env python

## file: wifi_sender.py
##
## package: wifi
##
## publishes: --
##
## subscribes to: user_input_topic
##
## description: senders user commands over wifi

import rospy
from std_msgs.msg import String
import constants
import socket
import sys

to_publish = "wifi_sender"

def start():
    HOST, PORT = "172.19.41.42", 15467
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    return sock

#connection functions
def AttemptConnection():
    true = true

def transmit(sock, data="test"):
    """ transmits data (str) to server; returns the string it receives"""

    sock.sendall(bytes(data))
    time.sleep(5)
    # Receive data from the server (returns a string)
    received = sock.recv(1024)

    rospy.loginfo("Sent: %s", data)
    rospy.loginfo("Received: {%s}", format(received))

    return received
 
def on_receive_user_input_topic(data):
    to_publish = data

def wifi_sender():
    rospy.init_node('wifi_sender', anonymous=False)

    rospy.Subscribe(user_input_topic, String, on_receive_user_input_topic)

    client = wificlient.start()

    while not rospy.is_shutdown():
        if to_publish: 
            if to_publish == "example_switch_stmt":
                wificlient.transmit(client, "example_publish")
            to_publish = ''
        else: wificlient.transmit()

if __name__ == '__main__':
    try: wifi_sender()
    except rospy.ROSInterruptException: pass

