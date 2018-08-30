#!/usr/bin/env python
# licensed under BSD-3


import rospy

from random import randint

from sensor_msgs.msg import JointState

import os
import sys
from os.path import dirname, abspath

#hacky way to add include directory to sys path
sys.path.append(os.path.join(dirname(dirname(abspath(__file__))),'include'))




convert to service
#def callback(data):

    
def inmoov_translator_input():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('inmoov_control_input', anonymous=False)

    rospy.Subscriber("joint_states", JointState, inmoov_translator_output)

    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()
    
    
def inmoov_translator_output():
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.name)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.position)
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    #rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
     #   hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo("publish something")
     #   pub.publish(hello_str)
        #rate.sleep()
        
        

if __name__ == '__main__':
    inmoov_translator_input()
    s
    
    
    