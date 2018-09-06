#!/usr/bin/env python
# licensed under BSD-3

import rospy
from sensor_msgs.msg import JointState
from inmoov_msgs.msg import MotorCommand

pub_r = rospy.Publisher('/joint_states_r', MotorCommand, queue_size=10)
#pub_l = rospy.Publisher('/joint_states_l', JointState)



def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y


def transform_callback(data):

    motorcommand = MotorCommand()
        
    motorcommand.id = 3
    motorcommand.value = mapFromTo(data.position[16], -0.09, 1.48, 30.0, 160.0)
    pub_r.publish(motorcommand)
    
    
        


def inmoov_splitter():
    rospy.init_node('inmoov_splitter', anonymous=True)
    rospy.Subscriber('joint_states', JointState, transform_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        inmoov_splitter()
    except rospy.ROSInterruptException:
        pass  
    
    
    
   