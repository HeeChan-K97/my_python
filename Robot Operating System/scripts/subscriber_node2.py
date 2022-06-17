#! usr/bin/env

from winreg import REG_OPTION_BACKUP_RESTORE
import rospy
from std_msgs.msg import String
from <name_of_package.msg> import Position


def callback(data):
    rospy.loginfo("%s X: %f  T: %f", data.message, data.x, data.y)#%s = placeholder for a message
#The reason for data.data: according to the documentation for String Message,
# the object name is called 'data' so to call string message inside data we need to say data.data
def listener():
    rospy.init_node("Subscriber_Node", anonymous=True)
    rospy.Subscriber('talking_topic', Position, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

#FINALLY we need to add onto our package.xml
#Uncomment the code saying
# = <exec_depend>message_runtime</exec_depend>
# = <build_depend>message_generation</build_depend>

#ALSO we need to add onto CMakelist

#On find_package add,
# message_generation
#Then uncomment line 50-54
    # add_message_files(
    #   FILES
    #   Position.msg
    # )
    # generate_message(
    #   DEPENDENCIES
    #   std_msgs
    # )

#As usual, catkin_make
# source devel/setup.bash
# roscore
# rosrun <package_name> publisher_node2.py
# rosrun <package_name> subscriber_node2.py
#Then we can receive what it means to