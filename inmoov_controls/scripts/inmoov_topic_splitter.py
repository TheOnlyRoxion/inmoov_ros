#!/usr/bin/env python
# licensed under BSD-3

import rospy
import time
from sensor_msgs.msg import JointState
from inmoov_msgs.msg import MotorCommand

pub_r = rospy.Publisher('/joint_states_r', MotorCommand, queue_size=10)
#pub_l = rospy.Publisher('/joint_states_l', MotorCommand, queue_size=10)


name=()
servoPin=()
minGoal=[]
maxGoal=[]
minIn=[]
maxIn=[]


def init():
    global name
    global servoPin
    global minGoal
    global maxGoal
    global minIn
    global maxIn
    time.sleep(20)
    for j,b in rospy.get_param('/joints').items():
        name+=j,
        servoPin+=rospy.get_param('/joints/' + j + '/servoPin',99),
        minGoal+=rospy.get_param('/joints/' + j + '/minGoal',30),
        maxGoal+=rospy.get_param('/joints/' + j + '/maxGoal',180),
        minIn+=rospy.get_param('/robot_description_planning/joint_limits/' + j + '/min_position',0),
        maxIn+=rospy.get_param('/robot_description_planning/joint_limits/' + j + '/max_position',0),
    rospy.loginfo("I found joints: %s with pin %s", name,servoPin)
 
 
def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y


def transform_callback(data):
    motorcommand = MotorCommand()  
    
    for i,n in enumerate(name):
        if n in data.name :
            if servoPin[i]<90:
                motorcommand.id = servoPin[i]
                motorcommand.value = mapFromTo(data.position[i], minIn[i],maxIn[i], minGoal[i], maxGoal[i])
                pub_r.publish(motorcommand)
                #rospy.loginfo("I move %s at Pin %s  to %s",n,motorcommand.id, motorcommand.value)

        


def inmoov_splitter():
    rospy.init_node('inmoov_splitter', anonymous=True)
    rospy.Subscriber('joint_states', JointState, transform_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        init()
        inmoov_splitter()
    except rospy.ROSInterruptException:
        pass  
    
    
    
   