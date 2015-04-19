#node that listens to the actuator sensor data and sends out a 
#soft-estop signal if necessary

import rospy
from soft_stop.msg import soft_stop_msg
from actuator.msg import actuator_sensor_msg

soft_stop_topic = "soft_stop_topic"
actuator_sensor_topic = "actuator_sensor_topic"
#is there a way to define constants within a package
#which would be visible to all of the nodes and which
#could be imported by nodes in other packages?

calibration_constant = 1.0
actuator_z_est = 0.0
safe_upper = 1.0    # 1  ft
safe_lower = -1.0   # -1 ft
#delta = 0.05        # how close to safe range for warn
warn_rate = 10  #Hz
warn_repeat = 5

def on_receive_sensor_data(data):
    actuator_z_est = data.height_offset * calibration_constant

def actuator_err():
    rospy.init_node('actuator_err', anonymous=False)

    rospy.Subscriber(actuator_sensor_topic, actuator_sensor_msg, on_receive_sensor_data)

    pub = rospy.Publisher(soft_stop_topic, soft_stop_msg, queue_size=10)
    rate = rospy.Rate(warn_rate)
    while not rospy.is_shutdown():
        #publish if outside of safe range
        if actuator_z_est > safe_upper or actuator_z_est < safe_lower:
            correction_dir = (actuator_z_est > safe_upper) ? "down" : "up"
            err = soft_stop_msg(actuator_err_bit=1, actuator_correction_dir=correction_dir)
            rospy.loginfo(err)
            for i in range(warn_repeat):
                pub.publish(err)
                rate.sleep()

if __name__ == '__main__':
    try:
        actuator_err()
    except rospy.ROSInterruptException:
        pass
