#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty,EmptyRequest

rospy.loginfo('starting the client')
rospy.init_node("my_caller")
rospy.wait_for_service("/global_localization")
my_connector=rospy.ServiceProxy("/global_localization",Empty)
my_call=EmptyRequest()
my_connector(my_call)