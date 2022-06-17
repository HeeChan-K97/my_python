import rospy
from <nameofpackage.srv> import multiplier, multiplierResponse

def callback(request):
    return multiplierResponse(request.a * request.b)

def multipy():
    rospy.init_node("multiplier_service")
    service == rospy.Service("multiplier", multiplier, callback)
    rospy.spin()

if __name__ == '__main__':
    multipy()


#CMAKELIST.TXT

#add_service_files(
#   FILES
#   multiplier.src
# )
#catkin_install_python(PROGRAMS scripts/publisher_node.py scripts/subscriber_node.py scripts/service_server_node.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )


#catkin_make
#source devel/setup.bach
#rosrun <nameofPkg> service_server_node.py
#rosservice list, we can see our service made "multiplier"
#rosservice info /multiplier
#rosservice call /multiplier and tab to call the arguments
#Then we can get the result through the function we defined