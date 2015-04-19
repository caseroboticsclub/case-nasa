execute_process(COMMAND "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/build/motor_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/build/motor_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
