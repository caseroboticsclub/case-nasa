# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "actuator: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iactuator:/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(actuator_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg/actuator_data.msg" NAME_WE)
add_custom_target(_actuator_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "actuator" "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg/actuator_data.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(actuator
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg/actuator_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/actuator
)

### Generating Services

### Generating Module File
_generate_module_cpp(actuator
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/actuator
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(actuator_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(actuator_generate_messages actuator_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg/actuator_data.msg" NAME_WE)
add_dependencies(actuator_generate_messages_cpp _actuator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(actuator_gencpp)
add_dependencies(actuator_gencpp actuator_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS actuator_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(actuator
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg/actuator_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/actuator
)

### Generating Services

### Generating Module File
_generate_module_lisp(actuator
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/actuator
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(actuator_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(actuator_generate_messages actuator_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg/actuator_data.msg" NAME_WE)
add_dependencies(actuator_generate_messages_lisp _actuator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(actuator_genlisp)
add_dependencies(actuator_genlisp actuator_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS actuator_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(actuator
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg/actuator_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator
)

### Generating Services

### Generating Module File
_generate_module_py(actuator
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(actuator_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(actuator_generate_messages actuator_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/actuator/msg/actuator_data.msg" NAME_WE)
add_dependencies(actuator_generate_messages_py _actuator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(actuator_genpy)
add_dependencies(actuator_genpy actuator_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS actuator_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/actuator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/actuator
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(actuator_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/actuator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/actuator
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(actuator_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/actuator
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(actuator_generate_messages_py std_msgs_generate_messages_py)
