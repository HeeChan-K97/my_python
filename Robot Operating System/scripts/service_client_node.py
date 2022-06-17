import rospy
from <nameofpackage.srv> import multiplier, multiplierResponse

def multiplier_client(x, y):
    rospy.init_node("client_node")
    rospy.wait_for_service("multiplier")#wait for a service called "multiplier" to exist in roscore
    rate = rospy.rate(1)
    while not rospy.is_shutdown():
        try:
            multiply_two_ints = rospy.ServiceProzy("multiplier", multiplier)#create an object for the service
            response = multiply_two_ints(x, y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print("Service call Failed %s", e)

if __name__ == '__main__':
    multiplier_client(7, 2)


#CMAKELIST.TXT

#catkin_install_python(PROGRAMS scripts/publisher_node.py scripts/service_client_node.py scripts/service_server_node.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

#catkin_make
#source devel/setup.bash
#rosrun <nameofpkg> service_server_node.py  //then we are now running the service
#rosrun <nameofpkg> service_client_node.py