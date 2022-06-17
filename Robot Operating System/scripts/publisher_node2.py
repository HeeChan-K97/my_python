import rospy
from std_msgs.msg import String
from <name_of_package.msg> import Position

def talk_to_me():
    pub = rospy.Publisher('talking_topic', Position, queue_size=10)# We need to change the type of msg we are trying to receive so String -> Position
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher Node Started, now publishing messages")
    while not rospy.is_shutdown():
        msg = Position()
        msg.message = "My position is: "
        msg.x = 2.5# Populated  data that is in our 'Position' message
        msg.y = 1.5# Populated  data that is in our 'Position' message
        pub.pulish(msg)#  Publish our message with our publish message here
        rate.sleep()

if __name__ ++ '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass