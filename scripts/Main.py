#!/usr/bin/python3
# -*- coding: UTF-8 -*-



import time
import socket
import cv2
from HandTrackingModule import HandDetector
import json
from time import sleep
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import sys
import tty
import termios
# import rospy
# from std_msgs.msg import String


# import sys
# import tty
# import termios
class Main:
    def __init__(self):
        self.camera = cv2.VideoCapture(1)
        self.camera.set(3, 740)
        self.camera.set(4, 740)
        # self.camera.set(5, 24)

        # 获取视频宽度
        self.frame_width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        # 获取视频高度
        self.frame_height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.camera.get(cv2.CAP_PROP_FPS)
        self.start_time = time.time()
        self.counter = 0
        self.i = 0
        self.detector = HandDetector()

    # def readchar():
    #     fd = sys.stdin.fileno()
    #     old_settings = termios.tcgetattr(fd)
    #     try:
    #         tty.setraw(sys.stdin.fileno())
    #         ch = sys.stdin.read(1)
    #     finally:
    #         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    #     return ch

    def Gesture_recognition(self):
        global src, i
        rospy.init_node("ma")
        pub= rospy.Publisher("ma",String,queue_size=10)
        while not rospy.is_shutdown():
            rate = rospy.Rate(10)
            msg = String()
           
            #pub2.publish(msg)
            # udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # # 使用套件字收发数据
            # # 目标IP 和端口，元组类型
            # ip_adders = ('127.0.0.1', 7788)
            # # msg = String()
            # # msg.data =i
            # # pub2.publish(msg)

            frame, img = self.camera.read()

            # self.counter += 1  # 计算帧数
            # if (time.time() - self.start_time) != 0:  # 实时显示帧数
            #     cv2.putText(img, "FPS {0}".format(float('%.1f' % (self.counter / (time.time() - self.start_time)))), (500, 50),
            #                 cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),
            #                 3)
            #     img = cv2.resize(img, (self.frame_width // 2, self.frame_height // 2),
            #                      interpolation=cv2.INTER_CUBIC)  # 窗口大小
            #     print("FPS: ", self.counter / (time.time() - self.start_time))
            img = self.detector.findHands(img)
            lmList, bbox = self.detector.findPosition(img)
            #     self.counter = 0
            #     self.start_time = time.time()

            if lmList:

                x_1, y_1 = bbox["bbox"][0], bbox["bbox"][1]
                x1, x2, x3, x4, x5 = self.detector.fingersUp()

                if (x2 == 1 and x3 == 1) and (x4 == 0 and x5 == 0 and x1 == 0):
                    cv2.putText(img, "Action_1", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    
                    msg.data ="2"
                    pub.publish(msg)
                elif (x2 == 1 and x3 == 1 and x4 == 1) and (x1 == 0 and x5 == 0):
                    cv2.putText(img, "Anti-Clockwise", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    msg.data ="3"
                    pub.publish(msg)
                elif (x2 == 1 and x3 == 1 and x4 == 1 and x5 == 1) and (x1 == 0):
                    cv2.putText(img, "Clockwise", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    msg.data ="4"
                    pub.publish(msg)
                elif x1 == 1 and x2 == 1 and x3 == 1 and x4 == 1 and x5 == 1:
                    cv2.putText(img, "Control", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    send_data = json.dumps(bbox["bbox"])

                    msg.data =send_data
                    pub.publish(msg)
                elif x2 == 1 and (x1 == 0, x3 == 0, x4 == 0, x5 == 0):
                    cv2.putText(img, "Action_initialization", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    msg.data ="1"
                    pub.publish(msg)
                elif x1 and (x2 == 0, x3 == 0, x4 == 0, x5 == 0):
                    cv2.putText(img, "Init", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    msg.data ="6"
                    pub.publish(msg)
            cv2.imshow("camera", img)
            if cv2.getWindowProperty('camera', cv2.WND_PROP_VISIBLE) < 1:
                break
            cv2.waitKey(1)

            # if cv2.waitKey(1) & 0xFF == ord("q"):
        #     break



if __name__ == '__main__':
    Solution = Main()
    Solution.Gesture_recognition()
