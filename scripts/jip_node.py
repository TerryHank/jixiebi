#!/usr/bin/env python3
#coding=utf-8
from time import sleep
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import sys
import tty
import termios
z=x=c=v=b=n=0

i=0.135
# def readchar() :
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch

def  callback(msg):
    global z,x,c,v,b,n
    print(type(msg))
    j=msg.data
    if   j == 'r':
      
        z +=i
    elif j  == 'f':
        z -=i
    elif j  == 't':
        x +=i
    elif j == 'g':
        x -=i
    elif j == 'y':
        c +=i
    elif j== 'h':
        c -=i
    elif j == 'u':
        v +=i
    elif j == 'j':
        v -=i
    elif j == 'i':
        b +=i
    elif j == 'k':
        b -=i
    elif j == 'o':
        n +=i
    elif j == 'l':
        n -=i
    elif j == 'q':
        sys.exit()
    elif j == '1':
        z,x,c,v,b,n=3,2,2,1,3,2

    elif j == '2':
        z,x,c,v,b,n=1,2,1,1,1,1

    elif j == '3':
        z +=i
    elif j == '4':
        z -=i    
    elif j == '6':
        z,x,c,v,b,n=1,2,1,1,1,1
        sleep(1)
        z,x,c,v,b,n=1,2,1,1,1,1
        
    elif type(eval(j)) is list :
        print(type(eval(j)))
    #          g1=0.007*(360-msg.data)
    # g2=360-tong()
    # zi(5.6,
    # 9.84+g1,
    # 3.61-g1,
    # 6.2,
    # 4.72,
    # 9.72 )  
                



        
if __name__ == "__main__":
    #pub2= rospy.Publisher("ma",String,queue_size=10)
    pub1 = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    sub = rospy.Subscriber("ma",String,callback,queue_size=10)
    while not rospy.is_shutdown():
       
        rate = rospy.Rate(10) # 10hz
        hello_str = JointState()
        hello_str.header = Header()
        hello_str.header.stamp = rospy.Time.now()
        hello_str.name = ['link1j', 'Link2j', 'Link3j', 'link4j','link5j','link6j']
       
        hello_str.position = [z,x,c,v,b,n]
        hello_str.velocity = []
        hello_str.effort = []
        # rospy.loginfo(msg.date )
        # msg = String()
        # msg.data =
        #pub2.publish(msg)
        pub1.publish(hello_str)
        rate.sleep() 
        