#node for interfacing with the actuator relay circuit
#listens to commands from commander node as well as 
#sensor feedback from the actuator sensor node

import rospy
#from std_msgs.msg import Float32
from commander.msg import commander_msg
#from actuator.msg import actuator_sensor_msg

#actuator_sensor_topic = "actuator_sensor_topic"
commander_topic = "high_commands"

#calibration_constant = 1.0

def on_receive_high_command(high_command):
    #parse command msg for part relevant to actuator
    actuator_toggle = high_command.toggle
    actuator_z_des  = high_command.actuator_z_des
    #based on this information, and on current position of
    #actuator (as estimated by the actuator_sensor), write
    #data to the necessary beagle_bone IO pins
    if actuator_toggle:
        #pid control on PRU- send desired state to BBB
        pass
    else:
        #make sure that actuator is not moving- send OFF to BBB
        pass

#def on_receive_sensor_data(data):
#    actuator_z_est = data.height_offset * calibration_constant
#    #data should really go straight to BBB for PID loop
#    #this is really just for soft-estop purposes, which
#    #should really be handled by another dedicated node

def actuator_driver():
    
    rospy.init_node('actuator_driver', anonymous=False)

    #rospy.Subscriber(actuator_sensor_topic, actuator_sensor_msg, on_receive_sensor_data)

    rospy.Subscriber(commander_topic, commander_msg, on_receiver_high_command)

    rospy.spin()

if __name__ == '__main__': 
    actuator_driver()
