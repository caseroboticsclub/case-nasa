#! /usr/bin/env python

## file: wifi_receiver.py
##
## package: wifi
##
## publishes: user_commands_topic
##
## subscribes to: --
##
## description: receivers user commands over wifi

import rospy
from std_msgs.msg import String
import constants
import socket
import sys
from thread import *

to_publish = "wifi_receiver"

#def on_receive_wifi_topic(data):
#    to_publish = data

def wifi_receiver():
    rospy.init_node('wifi_receiver', anonymous=False)
#    rospy.Subscribe(wifi_topic, String, on_receive_wifi_topic)
    pub = rospy.Publisher(user_commands_topic, String, queue_size=10)
    rate = rospy.Rate(10)

    sock = socketserve.start_socket() # initialize socket connection

    while not rospy.is_shutdown():
        conn, addr = sock.accept()
        event = socketserve.start_new_thread(socketserve.clientthread,(conn,))

        if event == "example_received": # equiv to hitting ESC or closing pygame window
            to_publish = event
        if event:
            pub.publish(to_publish)
            event = ''
        rate.sleep()

    sock.close()

if __name__ == '__main__':
    try: wifi_receiver()
    except rospy.ROSInterruptException: pass


def start_socket(): 
    """begins socket connection to client and returns the socket instance"""

    HOST = '192.168.0.100'   # Symbolic name meaning all available interfaces
    PORT = 8888              # Arbitrary non-privileged port
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rospy.loginfoi('Socket created')
 
    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error , msg:
        rospy.logerr('Bind failed. Error Code : %s Message %d', str(msg[0]), msg[1])
     
    rospy.loginfo('Socket bind complete')
 
    #Start listening on socket
    s.listen(10)
    rospy.loginfo('Socket now listening')

    return s
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    """waits until receives data from client then sends reply"""
    data  = ''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        reply = 'OK...' + data
        conn.sendall(reply)

    conn.close()
    return data

