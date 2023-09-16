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
SERVO_BAUDRATE = 115200 	# 舵机的波特率
SERVO_ID = 1 				# 舵机ID 
# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
					 parity=serial.PARITY_NONE, stopbits=1,\
					 bytesize=8,timeout=0)
# 创建舵机对象
uservo = UartServoManager(uart, servo_id_list=[SERVO_ID])

erro = [0,0,0,0,0,0,0,0,0,0]
times =  [0,0,0,0,0,0,0,0,0,0]
runtime_ms = 500
while(1):
    position = 0
    #舵机号1-5
    if SERVO_ID > 5:
        SERVO_ID = 1
        #system('cls')
    uservo.set_position_time(SERVO_ID, position, runtime_ms)
    #发送一次累加一次
    times[SERVO_ID-1]+=1
    print(f"向舵机:{SERVO_ID}发送{times[SERVO_ID-1]}次命令")

    time.sleep(1.3)
    # 读取数据
    position = uservo.read_data_by_name(SERVO_ID, "CURRENT_POSITION")
    if position is None :
        print(f"舵机:{SERVO_ID} 无法读取")
        SERVO_ID += 1
        continue
    if (position-0)>11:
        erro[SERVO_ID-1] += 1

    print(f"舵机:{SERVO_ID} 当前位置:  {position},错误：{erro[SERVO_ID-1]}次")
    time.sleep(0.2)

    position = 4095
    uservo.set_position_time(SERVO_ID, position, runtime_ms)
 
    time.sleep(1.3)
    # 读取数据
    position = uservo.read_data_by_name(SERVO_ID, "CURRENT_POSITION")
    if(position-4095)>11:
        erro[SERVO_ID-1] += 1
    print(f"舵机:{SERVO_ID} 当前位置:  {position},错误：{erro[SERVO_ID-1]}次")
    time.sleep(0.2)
    uservo.wait_all()
    SERVO_ID += 1
