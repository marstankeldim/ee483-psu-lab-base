cmake_minimum_required(VERSION 3.0.2)
project(lab1)

find_package(catkin REQUIRED COMPONENTS
  duckietown_msgs
  rospy
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/mmdriver.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
