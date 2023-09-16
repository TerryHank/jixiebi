#!/usr/bin/env python3
# coding=utf-8
import array
import socket
# import rospy
# from std_msgs.msg import String
from time import sleep
import sys
from pynput.keyboard import Key, Listener
import serial
# from sensor_msgs.msg import JointState
# from std_msgs.msg import Header
import sys
sys.path.append("/home/didi/catkin_ws/src/ji/scripts/srcs")
from data_table import TORQUE_DISABLE, TORQUE_ENABLE
import time
import serial
import struct
import sys
from uart_servo import UartServoManager
from data_table import *
import numpy as np
import rospy
from sensor_msgs.msg import JointState
times=1000



# 参数配置
SERVO_PORT_NAME = '/dev/ttyUSB0'  # 舵机串口号
SERVO_BAUDRATE = 115200  # 舵机的波特率

# 初始化串口
uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE, \
                     parity=serial.PARITY_NONE, stopbits=1, \
                     bytesize=8, timeout=0)
# 创建舵机对象
uservo = UartServoManager(uart)
def callback(msg):
    arr=np.array(msg.position)
    print(arr)
    arr0=arr[0]/0.0015
    arr1=(-arr[1]+1.5)/0.0016
    arr2=(arr[2]+3)/0.0015
    arr3=(arr[3]+3)/0.0015
    arr4=arr[4]/0.0015
    arr5=arr[5]/0.0015
    
    set_position(  arr0, arr1,  arr2,  arr3,  arr4,  arr5)

def tong():
    # 创建一个udp套件字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地相关信息，如果不绑定，则系统会随机分配，必须绑定本电脑的ip和port
    local_addr = ('', 7788)  # 元组的第一个参数为本机IP，可以为空字符串，会自动生成本机IP
    udp_socket.bind(local_addr)

    # 等待接收方发送数据
    # rs中存储的是一个元组（接收到的数据，（发送方的ip，port））
    rs_data = udp_socket.recvfrom(1024)
    rs_masg = rs_data[0]
    # rs_addr =rs_data[1]
    # print(rs_data)
    # #接收到的数据解码展示
    try:
        print(rs_masg.decode('utf-8'))
        color = eval(rs_masg.decode('utf-8'))[3]
        print(type(color))
        # 关闭套件字
        udp_socket.close()
        return color
    except:
        print(rs_masg.decode('utf-8'))
        color = rs_masg.decode('utf-8')
        # print(rs_addr)
        # 关闭套件字
        udp_socket.close()
        return color


def left1():
    position = uservo.read_data_by_name(1, "CURRENT_POSITION")
    uservo.set_position_time(1, position+100, 0)

def right1():
    position = uservo.read_data_by_name(1, "CURRENT_POSITION")
    uservo.set_position_time(1, position - 100, 0)

# def left2():
#
# def right2():
#
# def left3():
#
# def right3():
#
# def left4():
#
# def right4():
#
# def left5():
#
# def right5():
#
# def left6():
#
# def right6():

def y1():
    servo_id_list = [1, 2, 3, 4, 5]
    position_list = [0, 900, 2000, 2000, 0]
    runtime_ms_list = [1000, 1000, 1000, 1000, 1000]
    uservo.sync_set_position(servo_id_list, position_list, runtime_ms_list)
    # 等待所有舵机执行完成动作
    uservo.wait_all()


def y2():
    servo_id_list = [1, 2, 3, 4, 5]
    position_list = [0, 900, 2000, 2000, 0]
    runtime_ms_list = [1000, 1000, 1000, 1000, 1000]
    uservo.sync_set_position(servo_id_list, position_list, runtime_ms_list)
    # 等待所有舵机执行完成动作
    uservo.wait_all()


def y3():
    servo_id_list = [1, 2, 3, 4, 5]
    position_list = [0, 900, 2000, 2000, 0]
    runtime_ms_list = [1000, 1000, 1000, 1000, 1000]
    uservo.sync_set_position(servo_id_list, position_list, runtime_ms_list)
    # 等待所有舵机执行完成动作
    uservo.wait_all()


def y4():
    servo_id_list = [1, 2, 3, 4, 5]
    position_list = [0, 900, 2000, 2000, 0]
    runtime_ms_list = [1000, 1000, 1000, 1000, 1000]
    uservo.sync_set_position(servo_id_list, position_list, runtime_ms_list)
    # 等待所有舵机执行完成动作
    uservo.wait_all()


def Read_status():
    for SERVO_ID in [1, 2, 3, 4, 5]:
        position = uservo.read_data_by_name(SERVO_ID, "CURRENT_POSITION")
        print(f"舵机:{SERVO_ID} 当前位置:  {position}")


def set_position(a,b,c,d,e,f):
    servo_id_list = [1, 2, 3,4,5,6]
    position_list = [a, b, c,d,e,f]
    runtime_ms_list = [times, times, times,times,times,times]
    uservo.sync_set_position(servo_id_list, position_list, runtime_ms_list)

def zidong():
    y1
    sleep(2)
    y2
    sleep(2)
    y3
    sleep(2)
    y4
    sleep(2)


# def qianhou():
#     # global flag
#     # if tong()==360 or flag ==1:

#         g1=0.007*(360-tong())
#         # g2=360-tong()
#         zi(a1=5.6,a2=9.84+g1,a3=3.61-g1,a4=6.2,a5=4.72,a6=9.72)
#         flag =1

#         shifang()



def torque_disenable():
    for SERVO_ID in [1, 2, 3, 4, 5,6]:
        uservo.torque_enable(SERVO_ID, TORQUE_DISABLE)


def torque_enable():
    for SERVO_ID in [1, 2, 3, 4, 5,6]:
        uservo.torque_enable(SERVO_ID, TORQUE_ENABLE)


# def chao_callback():
#
# 	# aa=JointState.position[0]
# 	# bb=JointState.position[1]
# 	# cc=JointState.position[2]
# 	# dd=JointState.velocity[0]
# 	# ee=JointState.velocity[1]
# 	# ff=JointState.velocity[2]
# 	# print(aa,bb,cc,dd,ee,ff)

def shijiao():
    uservo.write_data_by_name(1, "GO2TECHING_POINT", 1)

def on_press(key):
    try:
        if key.char == "a":
            left1()
        if key.char == "s":
            right1()
        if key.char == "b":
            torque_disenable()
        if key.char == "c":
            torque_enable()

    except AttributeError:
        pass

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

if __name__ == "__main__":
    rospy.init_node('made')
    sub = rospy.Subscriber("joint_states",JointState,callback,queue_size=10)
    rospy.spin()
# rospy.signal_shutdown("qq")
