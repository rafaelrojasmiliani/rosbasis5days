#! /usr/bin/env python
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback


class cActionClient(object):
    def __init__(self):
        self.images_number_ = 1
        self.action_ = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)

    def feedback_callback(self, _feedback):
        rospy.loginfo('[Feedback] image n{:d} received'.format(self.images_number_))
        self.images_number_ += 1

    def execute_action_and_wait(self, _nsecods):
        self.execute_action(_nsecods)
        self.action_.wait_for_server()

    def execute_action(self, _nsecods):
        goal = ArdroneGoal()
        goal.nseconds = _nsecods 
        client.send_goal(goal, feedback_cb=self.feedback_callback)

def main():
    rospy.init_node('drone_action_client')
    action_client = cActionClient()
    action_client.execute_action(20)
    time.sleep(0.5)
    rospy.loginfo('It is asynchronous!!')
    status = action_client.action_.get_state()
    rospy.loginfo('The status is = {:d}'.format(status))
    action_client.action_.cancel_goal()  # would cancel the goal 3 seconds after starting
    rospy.loginfo('The status is = {:d}'.format(status))

