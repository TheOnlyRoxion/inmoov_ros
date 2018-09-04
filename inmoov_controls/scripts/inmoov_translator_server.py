#!/usr/bin/env python

from inmoov_controls.srv import InmoovTranslator
import rospy

def handle_inmoov_translator(req):
    pin = 2
    print "Returning [%s 'pin' %s ]"%(req.joint,pin)
   
    return pin

def inmoov_translator_server():
    rospy.init_node('inmoov_translator_server')
    s = rospy.Service('inmoov_translator',InmoovTranslator, handle_inmoov_translator)
    print "Ready to translate."
    rospy.spin()

if __name__ == "__main__":
    inmoov_translator_server()