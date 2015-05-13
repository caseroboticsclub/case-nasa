# list of topics and their publishers/subscribers

user_commands_topic = "user_commands_received" 
    publisher: wifi_receiver
    subscribers: commander 
    message_type: CommanderMsg

commander_topic = "high_commands" 
    publisher: commander
    subscribers: dig, belt, actuator, soft_estop, planning,
power_logger, slam (if want to override slam and tell the robot
where it is in the arena) 
    message_type: CommanderMsg
                  
		  bool estop
		  int64 actuator
		  int64 belt
		  int64 dig
		  int64[] drive
		  geometry_msgs/Pose loc (Point position, Quaternion orientation)
		  bool odom_reset
		  nav_msgs/Path planning

	**for portability, this is be a custom message so that there can be named fields for each of
	the nodes that subscribes to it (and can easily add/delete these fields as nodes are added/deleted). 
	Each of these fields is an int64 type (python int), and the subscribing nodes will use a case stmt (or
	equivalent) to decode the instruction (could also be an array int64[] for nodes with more complex functions).

soft_estop_topic = "soft_estop" 
    publisher: saber_monitor, commander, imu_processor 
    subscribers: soft_estop 
    message_type: bool 

saber_sender_topic = "saber_command_requests" 
    publisher: steering, dig, belt 
    subscribers: saber_sender_drive1, saber_sender_drive2, saber_sender_dig_belt
    message_type: int64[]
                    int64[0] = drive|dig|belt|override   # abstraction of the 'address' param
                    int64[1] = chan1|chan2|drive|turn|power|ramp|freewheel|stop
                    int64[2] = [-100,100] (% of max power) or other data

        **the % power is expressed like that so that the saber_sender can be more portable since different saber settings have different resolutions.

planning_topic = "planning_out" 
    publisher: planning 
    subscribers: steering, commander (so that user can query what the planner is
doing and so that commander can still issue commander_topic during
autonomous control) 
    message_type: nav_msgs/Path
                    Header header
                    geometry_msgs/PoseStamped[] poses

slam_topic = "slam_state_estimation" 
    publisher: slam 
    subscribers: planning, steering, commander 
    message_type: geometry_msgs/Pose loc 
                    Point position
                    Quaternion orientation

        **these will be in absolute terms referenced to the origin of the arena. That way, planning node can
        choose its own grid size to use. heading will be an (int) angle [0,360).

cumulative_odometry_topic = "cumulative_odometry" 
    publisher: odom
    subscribers: slam 
    message_type: float64[]
                    float64[0] = distance traveled (absolute)
                    float64[1] = which direction, really an int angle [0,360)

cumulative_odometry_reset_topic = "encoder_reset" 
    publisher: slam
    subscribers: odom 
    message_type: bool

imu_sensor_data_topic = "imu_sensor_data" 
    publisher: imu_sensor_listener 
    subscribers: imu_processor 
    message_type: IMUSensorMsg
                    Header header
                    geometry_msgs/Point accel
                    geometry_msgs/Point magn
                    geometry_msgs/Point gyro
                    float64 temp

        **would have had to define a custom msg anyways since sensor_msgs/IMU doesnt have temperature

imu_topic = "imu_data_processed" 
    publisher: imu_processor
    subscribers: slam 
    message_type: geometry_msgs/Pose

kinect_image_depth_topic = "kinect_depth_image" 
    publisher: kinect_processor_image_depth
    subscribers: obstacle_avoider
    message_type: float64[4] (affected area bounding box), int64 [-100, 100] normalized-(to what?)-how-deep

kinect_meta_topic = "kinect_camera_info" 
    publisher: kinect_processor_meta
    subscribers: obstacle_avoider
    message_type: float64 (camera angle, if this can be acquired from libfreenect (otherwise, this will be put in constants). the height of the camera off the ground will be a constant defined in the contants package since this can not be actively measured)

power_logging_topic = "power_data_processed" 
    publisher: power_analyzer
    subscribers: power_logger 
    message_type: float64 (power)

power_topic = "current_and_voltage" 
    publisher: any node collecting current (and voltage) data
    subscriber: power_analyzer 
    message_type: float64[]
                    float64[0] = current
                    float64[1] = voltage (if 0, nominal voltage estimate will be used)


