#! usr/bin/env

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("RECEIVED DATA: %s", data.data)
#The reason for data.data: according to the documentation for String Message,
# the object name is called 'data' so to call string message inside data we need to say data.data
def listener():
    rospy.init_node("Subscriber_Node", anonymous=True)
    rospy.Subscriber('talking_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

#callback function: function that will be calling every time when receive message from topic it is subscribing to
# everytime we make changes in the code we need to upload by typing catkin_make on terminal

#Operate the publisher and run the subscriber