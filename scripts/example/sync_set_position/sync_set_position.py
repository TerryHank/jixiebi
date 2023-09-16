'''
JOHO串口总线舵机 同步设置位置
--------------------------------------------------
- 作者: 阿凯爱玩机器人@成都深感机器人
- Email: xingshunkai@qq.com
- 更新时间: 2021-12-19
--------------------------------------------------
'''
# 添加uservo.py的系统路径
import sys
sys.path.append("/home/didi/catkin_ws/src/ji/scripts/srcs")

import time
import serial
import struct
import sys
from uart_servo import UartServoManager
from data_table import *
# 参数配置
SERVO_PORT_NAME =  '/dev/ttyUSB0' 	# 舵机串口号
SERVO_BAUDRATE = 115200 	# 舵机的波特率
SERVO_ID = 1 				# 舵机ID 
# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# 创建舵机对象
uservo = UartServoManager(uart, servo_id_list=[SERVO_ID])

# 同步写位置
servo_id_list = [1, 2, 3,4,5,6]
position_list = [900, 900, 2000,2000,0,0]
runtime_ms_list = [1000, 1000, 1000,1000,1000,1000]
uservo.sync_set_position(servo_id_list, position_list, runtime_ms_list)
# 等待所有舵机执行完成动作
uservo.wait_all()