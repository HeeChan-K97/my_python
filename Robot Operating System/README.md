This is a note for a ROS. Anything regarding the ROS tutorial and system can be noted down here.

Written By: HeeChan Kwon
Date start: 2022.06.17
Used Language: Python3
Related Team: FSAE

=============== HOW TO create workspace for ros and download package ===============

mkdir <file_name1>
cd <file_name1>
mkdir src

Then,,,
catkin_make

Then,,,
cd src
catkin_create_pkg <pkg_name> rospy std_msgs

#rospy std_msgs are dependencies

================ After creating the package and workspace ==================

create a new folder called scripts