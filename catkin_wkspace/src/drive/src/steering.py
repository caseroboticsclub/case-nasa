#! /usr/bin/env python

'''
 file: steering.py
 package: drive
 publishes: saber_sender_topic
 subscribes to: commander_topic
'''

import rospy
from std_msgs.msg import String
from commander.msg import CommanderMsg
from constants.src import constants

drive_command = None
last_drive_command = None
drive_sabers = [0,1]

def on_receive_commander_topic(command):
    global drive_command
    global last_drive_command
    last_drive_command = drive_command
    drive_command = command.drive

def steering():
    global drive_command
    global last_drive_command
    global drive_sabers

    rospy.init_node('steering', anonymous=False)
    rospy.Subscriber(commander_topic, CommanderMsg, on_receive_commander_topic)
    pub = rospy.Publisher(saber_sender_topic, int64[], queue_size=10)
    rate = rospy.Rate(50)
  
    while drive_command == None:
        rate.sleep()
    
    saber_send = [drive_command,0,0]

    while not rospy.is_shutdown():
        if last_drive_command[0] != drive_command[0]: # different power
            saber_send[2] = drive_command[0]
        if last_drive_command[1] != drive_command[1]: # different heading
            # consider adding a tolerance b/c overshoot is going to be HORRIBLE
            # scale the power based on the difference in headings
            saber_send[2] = scale_turning_power(drive_command[0], drive_command[1], last_drive_command[1])
            saber_send[1] = 3 # turn
        else: 
            saber_send[1] = 2 # drive
        pub.publish(saber_send)
        rate.sleep()

def scale_turning_power(req_power, heading, last_heading):
    scale_factor = abs(heading - last_heading) / 90.0
    return req_power * scale_factor

if __name__ == '__main__':
    try: steering()
    except rospy.ROSInterruptException: pass
