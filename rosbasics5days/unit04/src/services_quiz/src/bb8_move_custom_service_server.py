#! /usr/bin/env python
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
import numpy as np
                                                                                         
class cServiceServer(object):
    def __init__(self):
        self.srv_ = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , self.service) 
        self.pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.time_step_ = 0.001
        self.rate_ = rospy.Rate(1.0/self.time_step_)


    def service(self, *_data):
        request = _data[0]
        time_size_scale = 0.2
        repetitions = request.repetitions
        side = request.side*time_size_scale

        for _ in range(repetitions):
            for _ in range(4):
                self.move_linear(side)
                self.move_angular()

        my_response = BB8CustomServiceMessageResponse()
        my_response.success = True
        return  my_response 

    def move_linear(self, _side, _vel=0.2):
        command = Twist()
        command.linear.x = _vel
        displacement = 0.0
        while displacement < _side:
            self.pub_.publish(command)
            displacement += _vel*self.time_step_
#            rospy.loginfo('move linear {:.4f}'.format(displacement))
            self.rate_.sleep()
        command.linear.x = 0.0
        for _ in range(500):
            self.pub_.publish(command)
            self.rate_.sleep()

    def move_angular(self, _vel=0.2):
        command = Twist()
        command.angular.z = _vel
        displacement = 0.0
        while displacement < np.pi/4.0:
            self.pub_.publish(command)
#            rospy.loginfo('move angular {:.4f}'.format(displacement))
            self.rate_.sleep()
            displacement += _vel*self.time_step_
        command.angular.z = 0.0
        for _ in range(500):
            self.pub_.publish(command)
            self.rate_.sleep()


def main():
    rospy.init_node('service_client') 
    server = cServiceServer()
    rospy.spin() # mainta

if __name__ == '__main__':
    main()

