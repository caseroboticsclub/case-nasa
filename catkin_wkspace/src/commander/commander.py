# issue high level commands
# receive wifi commands under manual operation

import rospy
from std_msgs.msg import String

user_commands_topic = "user_commands_received"
commander_topic = "high_commands"

def on_receive_user_command(data):
    pass

def commander():
    pub = rospy.Publisher(commander_topic, String, queue_size=10)
    rospy.init_node('commander', anonymous=True)
    rate = rospy.Rate(10)
    rospy.Subscriber(user_commands_topic, String, on_receive_user_command)
    while not rospy.is_shutdown():
        # planning problem - use another python module
        info = "hello. %s" % rospy.get_time()
        rospy.loginfo(info)
        pub.publish(info)
        rate.sleep()

if __name__ == '__main__':
    try: 
        commander()
    except rospy.ROSInterruptException
        pass

