# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ex: 1 messages, 1 services")

set(MSG_I_FLAGS "-Iex:/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ex_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg/ex_msg.msg" NAME_WE)
add_custom_target(_ex_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ex" "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg/ex_msg.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/srv/ex_srv.srv" NAME_WE)
add_custom_target(_ex_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ex" "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/srv/ex_srv.srv" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ex
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg/ex_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ex
)

### Generating Services
_generate_srv_cpp(ex
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/srv/ex_srv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ex
)

### Generating Module File
_generate_module_cpp(ex
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ex
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ex_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ex_generate_messages ex_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg/ex_msg.msg" NAME_WE)
add_dependencies(ex_generate_messages_cpp _ex_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/srv/ex_srv.srv" NAME_WE)
add_dependencies(ex_generate_messages_cpp _ex_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ex_gencpp)
add_dependencies(ex_gencpp ex_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ex_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ex
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg/ex_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ex
)

### Generating Services
_generate_srv_lisp(ex
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/srv/ex_srv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ex
)

### Generating Module File
_generate_module_lisp(ex
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ex
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ex_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ex_generate_messages ex_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg/ex_msg.msg" NAME_WE)
add_dependencies(ex_generate_messages_lisp _ex_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/srv/ex_srv.srv" NAME_WE)
add_dependencies(ex_generate_messages_lisp _ex_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ex_genlisp)
add_dependencies(ex_genlisp ex_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ex_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ex
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg/ex_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ex
)

### Generating Services
_generate_srv_py(ex
  "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/srv/ex_srv.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ex
)

### Generating Module File
_generate_module_py(ex
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ex
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ex_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ex_generate_messages ex_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg/ex_msg.msg" NAME_WE)
add_dependencies(ex_generate_messages_py _ex_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/srv/ex_srv.srv" NAME_WE)
add_dependencies(ex_generate_messages_py _ex_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ex_genpy)
add_dependencies(ex_genpy ex_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ex_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ex)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ex
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(ex_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ex)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ex
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(ex_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ex)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ex\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ex
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(ex_generate_messages_py std_msgs_generate_messages_py)
