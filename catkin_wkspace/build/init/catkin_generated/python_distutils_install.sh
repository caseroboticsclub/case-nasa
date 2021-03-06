#!/bin/sh -x

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

cd "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/init"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
/usr/bin/env \
    PYTHONPATH="/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/install/lib/python2.7/dist-packages:/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/build" \
    "/usr/bin/python" \
    "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/init/setup.py" \
    build --build-base "/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/build/init" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/install" --install-scripts="/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/install/bin"
