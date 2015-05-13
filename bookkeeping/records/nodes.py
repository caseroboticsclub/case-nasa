def ui:
    '''handles the user interface. Pygame is used (from the COM room) to gather human input. This is converted into a 
        set of symbols (TODO: strings, chars, or ints) which are interpreted by the commander node.'''

def wifi_sender:
    '''handles the wifi connection between COM room and beagle bone. TWO options: 1. same method as last year, and 
        2. SSH into BBB. This node will only handle option 1. since SSHing can be taken care of dlirectly by the users.'''

def wifi_receiver:
    '''handles receiving option 1. data from COM room and redirecting the instructions it receives to the commander node.'''

def commander:
    '''receives instructions from wifi receiver node. delegates tasks to actuator, dig, belt, path-planning, and can also
        issue a soft-estop command. The commander is primarily for MANUAL control. Autonomous control is primarily handled 
        by the PLANNING node.'''

def power_logger:
    '''writes the results of the power analyzer to a file.'''

def planning:
    '''takes input from slam (really just 'l'), obstacle-avoider, and the commander to create a planned path for the robot.
        since we are trying not to rely on manual control, the path planner will have a general pre-defined (hard-coded) 
        plan that it should try to achieve, and really all it should need to do is make sure the robot does not run into
        things trying to execute it. 
        Roughly speaking, the plan will be to go straight from the initial position (after
        determining orientation, which can be done either via the magnometer or by the COM room sending a signal to the 
        robot telling it which of the 8 positions it started in) to the opposite side of the arena, turning to face the short
        length, moving back and forth 'X' times (1 <= X < 5) and then turning and moving back to the collector bin. Repeat
        until time runs out or no digging zone space left (each time, more less far into the digging area (first time, move
        as far as possible into it.
        The obstacle-avoider (via slam) and commander function as triggers to recalculate a path. slam triggers recalculation if
        1. the robot is judged to be significanly far off from where it is supposed to be, and 2. if the robot has reached
        the goal location and time has not run out.'''

def steering:
    '''uses real-time odom from the PRU and executes a PID loop using slam (actual) and path-planning (desired)'''

def timer:
    '''tracks the time used up so far in the 10-minute round. also averages the time taken for each run to determine whether
        path planning should start another iteration (traverse, dig, return), or the robot should gracefully shut down.'''

'''def actuator_middleman:
    '''deprecated. no sensor on actuator.'''
'''
def actuator_driver:
    '''toggles the relay circuit to drive the actuators for a specified time in a specified direction.'''

'''def motor_middleman:
    '''deprecated. useless.'''
'''
'''def motor_driver:
    '''deprecated. use saber-sender-tty instead.'''
'''
'''def velocity_profiler:
    '''deprecated. profiler built into saber 2x32.'''
'''
def dig:
    '''receives instructions from commander and planning which it relays to the saber-sender it shares with belt.'''

def belt:
    '''gets commands from commander and planning which it relays to the saber-sender it shares with dig.'''

'''def encoder_sensor_listener:
    '''deprecated. handled by PRU.'''
'''
'''def encoder_processor:
    '''deprecated. handled by PRU.'''
'''
def odom:
    '''handles output from PRU (encoder) and sends this cumulative odometry info to slam node.'''

def slam:
    '''uses cumulative odometry, magnometer reports to create an idea of where in the arena the robot currently is.'''

def obstacle_avoider:
    '''uses kinect info (image and physical state of camera) to locate obstacles. this is sent to slam, which keeps a record
        where all the obstacles in the arena are, and which can be used to trigger path-recalculation (handled by slam)'''

'''def current_sensor_listener:
    '''deprecated. use saber-monitor instead.'''

def current_sense_sensor_listener:
    '''deprecated. use saber-monitor instead.'''
'''
def saber_sender_tty:
    '''queues requests for saber commands so that it can subscribe to multiple topics (such as the saber that controls both the dig wheel and the conveyor belt)'''

def saber_monitor_tty:
    '''monitors current and voltage readings from the 3 saberteeth (6 motors). This should provide a good enough estimate of
        the power, unless we have additional current sensors (in which case, DO use the above nodes).
        if an error signal is received, triggers soft-estop.'''

def power_analyzer:
    '''takes current (and voltage) readings from the current-monitoring nodes and calculates the estimated power used so far.
        sends this estimate to the logging node.'''

'''def power_err:
    '''deprecated. see saber-monitor.'''
'''
def imu_sensor_listener:
    '''SPI interface for the IMU. Sends received data to the imu-processor.'''

def imu_processor:
    '''takes the magnometer reading from the imu-sensor and relays it to slam. takes the accelerometer reading and gives it to obstacle-avoider'''

'''def usbcam_sensor_listener:
    '''deprecated.'''

def usbcam_processor:
    '''deprecated.'''
'''
'''def kinect_sensor_listener:
    '''deprecated. let each kinect-processor topic subscribe to the kinect topic they need. (already have a driver for the 
        kinect from libfreenect'''
'''
def kinect_processor_image_depth:
    '''handles the depth image recieved from the kinect. used by the obstacle-avoider.'''

'''def kinect_image_processor_rgb:
    '''deprecated. was going to use this for localization but using cumulative odometry and magnometer only.'''
'''
def kinect_processor_meta:
    '''monitor (and/or control) physical state of the kinect sensor.'''

'''def actuator_sensor_listener:
    '''deprecated.'''

def actuator_processor:
    '''deprecated.'''

def actuator_err:
    '''deprecated.'''
'''
def soft_estop:
    '''triggered by commander, saber-monitor, and IMU-processor (accelerometer)'''

'''def load_cell_sensor_listener:
    '''deprecated.'''

def load_cell_processor:
    '''deprecated.'''
'''
