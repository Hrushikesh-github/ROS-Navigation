#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty
from nav_msgs.srv import GetMap,GetMapRequest
rospy.init_node("my_caller")
rospy.wait_for_service("/static_map")
my_connector=rospy.ServiceProxy("/static_map",GetMap)
my_call=GetMapRequest()
result=my_connector(my_call)
print(result)