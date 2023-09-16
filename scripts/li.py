#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['link1j', 'Link2j', 'Link3j', 'link4j','link5j','link6j']
    hello_str.position = [0,0,0,0,0,0]
    hello_str.velocity = []
    hello_str.effort = []
 
     
    pub.publish(hello_str)
    rate.sleep()

if __name__ == '__main__':
   while not rospy.is_shutdown():
        talker()

