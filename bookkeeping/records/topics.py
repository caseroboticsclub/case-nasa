# list of topics and their publishers/subscribers

user_input_topic = "user_keyboard_input" # user commands gathered from the keyboard in control room
    publisher: ui
    subscribers: wifi_sender
    message_type:

wifi_topic = "wifi"
    publisher: wifi_sender
    subscribers: wifi_receiver
    message_type:

user_commands_topic = "user_commands_received" # user commands after being received by robot over wifi
    publisher: wifi_receiver
    subscribers: commander
    message_type:

commander_topic = "high_commands"
    publisher: commander
    subscribers: dig, planning, power_logger
    message_type:

soft_estop_topic = "soft_estop"
    publisher: actuator_err, power_err, commander
    subscribers: soft_estop
    message_type:

actuator_sensor_data_topic = "actuator_sensor_data"
    publisher: actuator_sensor_listener
    subscribers: actuator_processor
    message_type:

actuator_topic = "actuator_data_processed"
    publisher: actuator_processor
    subscribers: actuator_err, slam
    message_type:

steering_topic = "steering_out"
    publisher: steering
    subscribers: motor_middleman, actuator_middleman
    message_type:

revised_actuator_velocity_topic = "revised_actuator_velocity"
    publisher: actuator_middleman
    subscribers: actuator_velocity_profiler
    message_type:

revised_motor_velocity_topic = "revised_motor_velocity"
    publisher: motor_middleman
    subscribers: motor_velocity_profiler
    message_type:

profiled_actuator_velocity_topic = "profiled_actuator_velocity"
    publisher: actuator_velocity_profiler
    subscribers: actuator_driver
    message_type:

profiled_motor_velocity_topic = "profiled_motor_velocity"
    publisher: motor_velocity_profiler
    subscribers: motor_driver
    message_type:

final_actuator_velocity_topic = "final_actuator_velocity"
    publisher:
    subscribers:
    message_type:

final_motor_velocity_topic = "final_motor_velocity"
    publisher:
    subscribers:
    message_type:

planning_topic = "planning_out"
    publisher: planning
    subscribers: steering, commander
    message_type:

slam_topic = "slam_state_estimation"
    publisher: slam
    subscribers: planning, steering
    message_type:

encoder_sensor_data_topic = "encoder_sensor_data"
    publisher: encoder_sensor_listener
    subscribers: encoder_processor
    message_type:

encoder_topic = "encoder_data_processed"
    publisher: encoder_processor
    subscribers: odom
    message_type:

odometry_topic = "odometry_state_estimation"
    publisher: odom
    subscribers: slam
    message_type:

# make this a service?
encoder_reset_topic = "encoder_reset"
    publisher: odom
    subscribers: encoder
    message_type:

imu_sensor_data_topic = "imu_sensor_data"
    publisher: imu_sensor_listener
    subscribers: imu_processor
    message_type:

imu_topic = "imu_data_processed"
    publisher: imu_processor
    subscribers: slam
    message_type:

kinect_sensor_data_topic = "kinect_sensor_data"
    publisher: kinect_listener
    subscribers: kinect_processor
    message_type:

kinect_topic = "kinect_data_processed"
    publisher: kinect_processor
    subscribers: slam
    message_type:

usbcam_sensor_data_topic = "usbcam_sensor_data"
    publisher: usbcam_listener(1/2/.../n)
    subscribers: usbcam_processor
    message_type:

usbcam_topic = "usbcam_data_processed"
    publisher: usbcam_processor
    subscribers: slam
    message_type:

current_sensor_data_topic = "current_sensor_data"
    publisher: current_sensor_listener
    subscribers: power_analyzer
    message_type:

current_sense_sensor_data_topic = "current_sense_sensor_data"
    publisher: current_sense_sensor_listener
    subscribers: power_analyzer
    message_type:

power_topic = "power_data_processed"
    publisher: power_analyzer
    subscribers: power_logger, power_err
    message_type:

load_cell_sensor_data_topic = "load_cell_sensor_data"
    publisher: load_cell_sensor_listener
    subscribers: load_cell_processor
    message_type:

load_cell_topic = "load_cell_data_processed"
    publisher: load_cell_processor
    subscribers: 
    message_type:
