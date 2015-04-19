#! /usr/bin/env python

## file: constants.py
##
## package: constants
##
## publishes: --
##
## subscribes to: --
##
## description: defines constants used by other packages

## topics ##
user_input_topic            = "user_keyboard_input"
wifi_topic                  = "wifi"
user_commands_topic         = "user_commands_received"
commander_topic             = "high_commands"
soft_estop_topic             = "soft_estop"
actuator_sensor_data_topic  = "actuator_sensor_data"
actuator_topic              = "actuator_data_processed"
revised_motor_velocity_topic = "revised_motor_velocity"
profiled_motor_velocity_topic = "profiled_motor_velocity"
revised_actuator_velocity_topic = "revised_actuator_velocity"
profiled_actuator_velocity_topic = "profiled_actuator_velocity"
steering_topic              = "steering_commands_out"
planning_topic              = "planning_out"
slam_topic                  = "slam_state_estimation"
encoder_sensor_data_topic   = "encoder_sensor_data"
encoder_topic               = "encoder_data_processed"
odometry_topic              = "odometry_state_estimation"
encoder_reset_topic         = "encoder_reset"
imu_sensor_data_topic       = "imu_sensor_data"
imu_topic                   = "imu_data_processed"
kinect_sensor_data_topic    = "kinect_sensor_data"
kinect_topic                = "kinect_data_processed"
usbcam_sensor_data_topic    = "usbcam_sensor_data"
usbcam_topic                = "usbcam_data_processed"
current_sensor_data_topic   = "current_sensor_data"
current_sense_sensor_data_topic = "current_sense_sensor_data"
power_topic                 = "power_data"

## variables ##
actuator_upper_limit = 1
actuator_lower_limit = -1

