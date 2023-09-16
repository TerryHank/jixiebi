'''
JOHO串口总线舵机 - 异步写
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


position = 1000
runtime_ms = 500
uservo.async_set_position(SERVO_ID, position, runtime_ms)
# 这里写其他舵机的 async_set_position, 举例子：
SERVO_ID = 2
uservo.async_set_position(SERVO_ID, position, runtime_ms)

# 统一开始执行
uservo.async_action()

# 等待所有舵机执行完成动作
uservo.wait_all()
