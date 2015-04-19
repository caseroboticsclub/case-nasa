#global variables and other global settings

commander_topic = "high commands"

actuator_sensor_data_topic = "actuator_sensor_data"

soft_estop_topic = "soft_estop"

user_commands_topic = "user_commands_received" # user commands after being received by robot over wifi

imu_sensor_topic = "imu_sensor_data"

kinect_sensor_data_topic = "kinect_sensor_data"

desired_velocity_topic = "desired_velocity"  # repackaged commander commands sent to steering node

steering_topic = "steering_commands_out"    # output of steering node 

revised_velocity_topic = "revised_velocity" # result of steering algorithm sent to velocity profiler node

velocity_profiler_topic = "velocity_profiler_out"   # output of velocity profiler node

odometry_topic = "odometry_state_estimation"

encoder_topic = "motor_encoder_vel_heading_distance"

# should be a service
encoder_distance_reset_topic = "motor_encoder_distance_reset"

planning_topic = "planning"

slam_topic = "slam_state_estimation"

user_input_topic = "user_keyboard_input" # user commands gathered from the keyboard in control room

usbcam_data_topic = "usbcam_data"
