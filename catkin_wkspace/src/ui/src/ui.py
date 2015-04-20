#! /usr/bin/env python

## file: ui.py
##
## package: ui
##
## publishes: user_input_topic
##
## subscribes to: --
##
## description: harvests user input and sends it along
## its merry way.

import rospy
from stdmsgs.msg import String
import constants
import pygame

def STDIN():
    event = pygame.event.wait()
    if event.type == pygame.QUIT: 
        #return ...
    elif event.type == pygame.KEYDOWN:
        #if event.key == ...
            #if pygame.key.get_mods() & shift: ...
        pass        
    elif event.type == pygame.KEYUP:
        pass
    #elif....
    else:
        return ''

def ui():
    rospy.init_node('ui', anonymous=False)
    
    pub = rospy.Publisher(user_input_topic, String, queue_size=10)
    rate = rospy.Rate(10)
    
    pygame.display.set_mode((100,100)) # empty screen- helps event handling
    pygame.init()

    while not rospy.is_shutdown():
        to_publish = STDIN()
        pub.publish(to_publish)
        pygame.display.flip()
        #rate.sleep()

    pygame.quit()

if __name__ == '__main__':
    try: ui()
    except rospy.ROSInterruptException: pass

