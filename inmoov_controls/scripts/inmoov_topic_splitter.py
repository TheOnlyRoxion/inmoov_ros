#!/usr/bin/env python
# licensed under BSD-3

import time
import rospy
from sensor_msgs.msg import JointState
from inmoov_msgs.msg import MotorCommand

pub_r = rospy.Publisher('/joint_states_r', MotorCommand, queue_size=10)
pub_l = rospy.Publisher('/joint_states_l', MotorCommand, queue_size=10)


NAME = ()
SERVO_PIN = ()
MIN_GOAL = ()
MAX_GOAL = ()
MIN_IN = ()
MAX_IN = ()
BUS = ()


def init():
    global NAME
    global SERVO_PIN
    global MIN_GOAL
    global MAX_GOAL
    global MIN_IN
    global MAX_IN
    global BUS
    time.sleep(1)
    for j,b in rospy.get_param('/joints').items():
        NAME += j,
        SERVO_PIN += rospy.get_param('/joints/' + j + '/servoPin', 99),
        MIN_GOAL += rospy.get_param('/joints/' + j + '/minGoal', 40),
        MAX_GOAL += rospy.get_param('/joints/' + j + '/maxGoal', 40),
        BUS += rospy.get_param('/joints/' + j + '/bus', 0),
        MIN_IN += rospy.get_param('/robot_description_planning/joint_limits/' + j + '/min_position', 0),
        MAX_IN += rospy.get_param('/robot_description_planning/joint_limits/' + j + '/max_position', 0),
#rospy.loginfo("I found joints: %s with pin %s with input range %s / %s and output range %s / %s", name,servoPin,minIn,maxIn,minGoal,maxGoal)


def map_from_to(x,a,b,c,d):
    y = (x-a)/(b-a)*(d-c)+c
    return y


def transform_callback(data):
    """here the magic happens"""
    global NAME
    global SERVO_PIN
    global MIN_GOAL
    global MAX_GOAL
    global MIN_IN
    global MAX_IN
    global BUS

    motorcommand = MotorCommand()

    for i, n in enumerate(NAME, 0):
        if n in data.name :
            if SERVO_PIN[i]<90:
                if BUS[i]==1:
                    motorcommand.id = SERVO_PIN[i]
                    motorcommand.value = map_from_to(data.position[data.name.index(n)], MIN_IN[i],MAX_IN[i], MIN_GOAL[i], MAX_GOAL[i])
                    pub_r.publish(motorcommand)
                if BUS[i]==2:
                    motorcommand.id = SERVO_PIN[i]
                    motorcommand.value = map_from_to(data.position[data.name.index(n)], MIN_IN[i],MAX_IN[i], MIN_GOAL[i], MAX_GOAL[i])
                    pub_l.publish(motorcommand)
                #rospy.loginfo("I move %s at Pin %s  to %s",n,motorcommand.id, motorcommand.value)


def inmoov_splitter():
    """init_node"""
    rospy.init_node('inmoov_splitter', anonymous=True)
    rospy.Subscriber('joint_states', JointState, transform_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        init()
        inmoov_splitter()
    except rospy.ROSInterruptException:
        pass
