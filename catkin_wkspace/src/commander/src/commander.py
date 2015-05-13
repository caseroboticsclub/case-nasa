#! /usr/bin/env python

'''
 file: commander.py
 package: commander 
 publishes: commander_topic (type: CommanderMsg)
 subscribes to: user_commands_topic (type: CommanderMsg)
                slam_topic          (type: geometry_msgs/Pose)
                planning_topic      (type: nav_msgs/Path)
'''

import rospy
from commander.msg import CommanderMsg
from constants.src import constants
import math

# global variables
init = False
flag_user = False
recvd_commands = None     # type CommanderMsg
recvd_loc = None          # type geometry_msgs/Pose
recvd_plan = None         # type nav_msgs/Path

can_dig_Y = 4.44  # start zone: 1.5m   obstacle zone: 2.94m

# the following should be declared in 'constants' so other nodes can use them too
robot_X = 0.75  # meters, need to divide by 2
robot_Y = 1.50  # meters, need to divide by 2
arena_X = 3.78  # meters
arena_Y = 7.38  # meters

def on_receive_user_commands_topic(data):
    global init
    global flag_user
    init = True
    flag_user = True
    recvd_commands = data

def on_receive_slam_topic(message):
    global init
    init = True
    recvd_loc = message

def on_receive_planning_topic(message):
    recvd_plan = message

def commander():
    
    global init
    global recvd_commands
    global recvd_loc
    global recvd_plan
    global flag_user
    
    rospy.init_node('commander', anonymous=True)
    pub = rospy.Publisher(commander_topic, CommanderMsg, queue_size=10)
    rate = rospy.Rate(10)
    rospy.Subscriber(user_commands_topic, CommanderMsg, on_receive_user_commands_topic)

    # bash script to launch the launch files will ensure that this is the last node.
    # needs to get initial position before issuing any commands
    while not init:
        rate.sleep() # something harmless to do

    # we now have an initial position contained in either recvd_commands or recvd_loc
    commands = construct_initial_commands(recvd_commands, recvd_loc)

    flag_user = False
    next_goal = 0
    
    while not rospy.is_shutdown():
        pub.publish(commands)
        commands = construct_next_commands(recvd_commands, flag_user, 
                                           recvd_loc, recvd_plan, next_goal, commands)
        rate.sleep()

'''construct the first set of commands based on the initial location'''
def construct_initial_commands(recvd_commands, recvd_loc):
    initial_commands = CommanderMsg()

    return initial_commands

'''construct the next set of commands based on all messages received, 
if those messages have been updated, and last set of commands issued'''
def construct_next_commands(recvd_commands, flag_user, 
                            recvd_loc, recvd_plan, next_goal, commands):
    next_commands = commands
    # based on the recvd_loc and recvd_plan, calculate what the next action should be
    # is the robot in the digging area?
    if can_dig(recvd_loc):
        next_commands.dig = True
        next_commands.actuator = -1    # state=down
        next_commands.drive[0] = 10    # speed for digging, 10% of max power
    else:
        next_commands.actuator = 1      # state=up
        next_commands.dig = False
        next_commands.drive[0] = 25     # speed for normal activity, 25% of max power
    ###todo: how to tell if stuck? need to subscribe to obstacle_topic and increase power if stuck

    # where is the robot in relation to the next intermediate goal location?
    next_heading = evaluate_target(recvd_loc, recvd_plan, next_goal)
    if next_heading < 0:
        next_commands = wait()
        rospy.logwarn('waiting for a new path to be calculated')
    if flag_user: 
        global flag_user
        flag_user = False   # I wonder if this will cause syncing issues...
        # override all non-null fields
        if recvd_commands.estop != None: next_commands.estop = recvd_commands.estop
        if recvd_commands.actuator != None: next_commands.actuator = recvd_commands.actuator
        if recvd_commands.dig != None: next_commands.dig = recvd_commands.dig
        if recvd_commands.belt != None: next_commands.belt = recvd_commands.belt 
        if recvd_commands.drive != None: next_commands.drive = recvd_commands.drive 
        if recvd_commands.loc != None: next_commands.loc = recvd_commands.loc 
        if recvd_commands.odom_reset != None: next_commands.odom_reset = recvd_commands.odom_reset 
        if recvd_commands.planning != None: next_commands.planning = recvd_commands.planning 
    return next_commands

'''return True if 1. within the digging zone, 2. facing in the mostly (+-)X direction.
    @param geometry_msgs/Pose loc   the current location of the robot
    @return bool    is the robot allowed to dig in its current position'''
def can_dig(loc):
    global can_dig_Y # this will change based on the iteration 
    global arena_Y
    global arena_X
    global robot_Y
    global robot_X

    wall_thresh = 0.5   # meters, distance away from the wall not to dig within
   
    if ((loc.position.x - (robot_X/2.0)) < wall_thresh) or 
        ((loc.position.x + (robot_X/2.0)) > (arena_X - wall_thresh)):
        return False
    if (loc.position.y + (robot_Y/2.0)) <= can_dig_Y:
        return False
    x = loc.orientation.x
    if (x > 45 and x < 135) or (x > 225 and x < 315):
        return False
    return True

'''based on the current location and the next step in the path, what direction should the 
    robot head in order to stay on target?
    @param geometry_msgs/Pose recvd_loc    the current location
    @param nav_msgs/Path recvd_plan     the proposed plan
    @param int next_goal    next index into the planned path 
    @return int     the revised heading [0,360)'''
def evaluate_target(recvd_loc, recvd_plan, next_goal):
    heading = recvd_loc.orientation.x
    x, y = recvd_loc.position.x, recvd_loc.position.y
    if next_goal >= len(recvd_plan): return -1  # need to recalculate a new plan ASAP!
    next_pose = recvd_plan[next_goal]
    
    # does the target position lie within a tolerane of the current line of travel?
    goal_x, goal_y = next_goal.pose.position.x, next_goal.pose.position.y
    dx = goal_x - x
    dy = y - goal_y - y
    dh = round(math.pi * (math.atan2(dy, dx)) / 180.0)
    heading += dh
    
    # is the robot close enough to this goal to move on to the next goal?
    global robot_X
    goal_tolerance = robot_X / 4.0
    mag = math.sqrt(dx*dx + dy*dy)
    if mag < goal_tolerance:
        goal += 1
    
    return heading

'''if the robot is unsure what to do, wait for further instructions, stop all motors.
    @return CommanderMsg    the wait command'''
def wait():
    global recvd_loc
    wait = CommanderMsg()
    wait.estop = False
    wait.actuator = 1
    wait.dig = 0
    wait.belt = 0
    wait.drive = [0,recvd_loc.orientation.x]
    wait.loc = recvd_loc
    wait.odom_reset = False
    wait.planning = None    # signal to calculate a plan
    return wait

if __name__ == '__main__':
    try: commander()
    except rospy.ROSInterruptException: pass

