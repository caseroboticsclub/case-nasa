#! /usr/bin/env python

## file: kinect_processor.py
##
## package: kinect
##
## publishes: kinect_topic
##
## subscribes to: kinect_sensor_data_topic
##
## description: transforms kinect sensor data into meaningful 
## information

import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
#import constants
import numpy, cv2

once=0

# data is of type sensor_msgs/Image:
# std_msgs/Header header
#   uint32 seq
#   time stamp
#   string frame_id
# uint32 height
# uint32 width
# string encoding
# uint8 is_bigendian
# uint32 step
# uint8[] data
def on_receive_kinect_sensor_data_topic(data):
    # write the data to a file for openCV processing    
    # a grayscale image in cv2 is a numpy array of uint8
    global once
    if not once and not (data.data==None or data.data == ''):
#        gray = numpy.array(data.data)
        print("kinect depth image: height=%d, width=%d, dtype=%s of %s"%(data.height, data.width, type(data.data), type(data.data[0])))
        print(data.data)
        na = numpy.uint8(data.data)
        #numpy.savetxt(f, na, fmt='%d', delimiter=',', comments='') 
        #na.tofile(g, sep=",", format="%d")
        cv2.imwrite('g.png', na)
        global once
        once = 1

def kinect_processor():
    rospy.init_node('kinect_processor', anonymous=False)
    # pub = rospy.Publisher(kinect_topic, ? , 10, queue_size=10)
    # rospy.rate(10)
    rospy.Subscriber("/camera/depth/image", Image, on_receive_kinect_sensor_data_topic)
    
    rospy.spin()    # need to publish something

if __name__ == '__main__':
    try: kinect_processor()
    except rospy.ROSInterruptException: pass
 
