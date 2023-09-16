'''
JOHO舵机测试
'''
# 添加uservo.py的系统路径
from os import system
import sys
from turtle import delay
sys.path.append("./src")

import time
import serial
import struct
import sys
from uart_servo import UartServoManager
from data_table import *
# 参数配置
SERVO_PORT_NAME =  '/dev/ttyUSB0' 	# 舵机串口号
#SERVO_PORT_NAME =  'COM6' 	# win舵机串口号
SERVO_BAUDRATE = 115200 	# 舵机的波特率
SERVO_ID_1 = 1 				# 舵机ID 1
SERVO_ID_2 = 2				       # 舵机ID 2
# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# 创建舵机对象
uservo = UartServoManager(uart)
# #servo_id_list,用于检测列表上的舵机是否在线
# servo_id_list=[1,2,3]
# uservo = UartServoManager(uart,servo_id_list)
position = 0
runtime_ms = 500
uservo.set_position_time(SERVO_ID_1, 2048, runtime_ms)
time.sleep(0.01)
uservo.set_position_time(SERVO_ID_2, 2048, runtime_ms)
time.sleep(0.8)

#start
# 读取数据1
position = uservo.read_data_by_name(SERVO_ID_1, "CURRENT_POSITION")
time.sleep(0.01)
if position is not None:
# 执行+45度
	uservo.set_position_time(SERVO_ID_1, position+512, 1000)
	time.sleep(3)

position = uservo.read_data_by_name(SERVO_ID_2, "CURRENT_POSITION")
time.sleep(0.01)

if position is not None:
# 执行-30度
	uservo.set_position_time(SERVO_ID_2, position-341, 1000)

