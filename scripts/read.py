#!/usr/bin/env python3
import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
sys.path.append("/home/didi/catkin_ws/src/ji/scripts/srcs")

import time
import serial
import struct
import sys
from uart_servo import UartServoManager
from data_table import *
from time import sleep

# 参数配置
SERVO_PORT_NAME =  '/dev/ttyUSB0' 	# 舵机串口号
SERVO_BAUDRATE = 115200 	# 舵机的波特率
SERVO_ID = 1 			# 舵机ID 
# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# 创建舵机对象
uservo = UartServoManager(uart, servo_id_list=[SERVO_ID])

def talker():
	pub1 = rospy.Publisher('joint_states', JointState, queue_size=10)
	rospy.init_node('joint_state_publisher')
	position1 = uservo.read_data_by_name(1, "CURRENT_POSITION")*0.00314-1.5
	position2 = -(uservo.read_data_by_name(2, "CURRENT_POSITION")*0.0016-1.5)
	position3 = uservo.read_data_by_name(3, "CURRENT_POSITION")*0.0015-3
	position4 = uservo.read_data_by_name(4, "CURRENT_POSITION")*0.0015-3
	position5 = uservo.read_data_by_name(5, "CURRENT_POSITION")
	position6 = uservo.read_data_by_name(6, "CURRENT_POSITION")
	rate = rospy.Rate(10) # 10hz
	hello_str = JointState()
	hello_str.header = Header()
	hello_str.header.stamp = rospy.Time.now()
	hello_str.name = ['link1j', 'Link2j', 'Link3j', 'link4j','link5j','link6j']
	print(position1 ,position2 ,position3 ,position4 ,position5 ,position6 )

	hello_str.position = [position1 ,position2 ,position3 ,position4 ,position5 ,position6 ]
	hello_str.velocity = []
	hello_str.effort = []
	# rospy.loginfo(msg.date )
	# msg = String()
	# msg.data =
	#pub2.publish(msg)
	pub1.publish(hello_str)
	rate.sleep() 

# 读取数据
if __name__ == '__main__':
	while not rospy.is_shutdown():
		talker()


