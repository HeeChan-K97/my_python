#! usr/bin/env
# execute script as python does

import rospy
from std_msgs.msg import String

def talk_to_me():
    pub = rospy.Publisher('talking_topic', String, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher Node Started, now publishing messages")
    while not rospy.is_shutdown():
        msg = "Hello HeeChan - %s" % rospy.get_time()
        pub.pulish(msg)
        rate.sleep()

if __name__ ++ '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass

#below the catkin_package messages in CMakeLists we add,,,
# catkin_install_python(PROGRAMS scripts/publisher_node.py
# DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

# Then we do catkin_make
# Then source devel/setup.bash
# THen run roscore for master
# Then rosrun <name_package> publisher_node.py
# Then we will get INFO message

# We can test and see rostopic list to see what topic is running
# rostopic echo /talking_topic
# Then we can communicate with the topic