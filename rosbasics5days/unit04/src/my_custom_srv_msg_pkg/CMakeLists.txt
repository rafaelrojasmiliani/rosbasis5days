cmake_minimum_required(VERSION 2.8.3)
project(my_custom_srv_msg_pkg)
find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)
add_service_files(
  FILES
  MyCustomServiceMessage.srv
)
generate_messages(
  DEPENDENCIES
  std_msgs
)
catkin_package(
  CATKIN_DEPENDS rospy message_runtime
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
