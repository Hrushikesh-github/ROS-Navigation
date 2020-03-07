'''
 the code for an Action Client in order to send messages to the Action Server of the move_base node
 '''
#! /usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal,MoveBaseFeedback,MoveBaseResult

rospy.init_node('drone_action_client')
# create the connection to the action server
client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
# waits until the action server is up and running
client.wait_for_server()
# creates a goal to send to the action server
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = 'map'
goal.target_pose.pose.orientation.w=0.75
goal.target_pose.pose.orientation.z=0.66

state_result=client.get_state()
i=0
def feedback_callback(feedback):
    rospy.loginfo("On way to goal")
rospy.loginfo("Starting to move")
while i<3:
    if i==0:
        goal.target_pose.pose.position.x = 3.02 # indicates, take pictures along 10 seconds
        goal.target_pose.pose.position.y = -3.14

        client.send_goal(goal, feedback_cb=feedback_callback)
        client.wait_for_result()
        i+=1
    elif i==1:
        goal.target_pose.pose.position.x = 2.5764 # indicates, take pictures along 10 seconds
        goal.target_pose.pose.position.y = 1.93

        client.send_goal(goal, feedback_cb=feedback_callback)
        client.wait_for_result()
        i+=1
    elif i==2:
        goal.target_pose.pose.position.x = -3.5859 # indicates, take pictures along 10 seconds
        goal.target_pose.pose.position.y = 1.518

        client.send_goal(goal, feedback_cb=feedback_callback)
        client.wait_for_result()
        i=0
