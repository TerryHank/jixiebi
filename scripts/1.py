# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.
@ by: caixy
@ date: 2021-10-1

"""
import time

import cv2
from HandTrackingModule import HandDetector
import rospy
from std_msgs.msg import String
# import sys
# import tty
# import termios
class Main:
    def __init__(self):
        self.camera = cv2.VideoCapture(1)
        self.camera.set(3, 1280)
        self.camera.set(4, 740)
        # self.camera.set(5, 24)

        # 获取视频宽度
        self.frame_width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        # 获取视频高度
        self.frame_height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.camera.get(cv2.CAP_PROP_FPS)
        self.start_time = time.time()
        self.counter = 0
        self.i=0
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
        global src,i
        pub2= rospy.Publisher("ma",String,queue_size=10)
        rospy.init_node('mama')
        while not rospy.is_shutdown():
            rate = rospy.Rate(50)
            # msg = String()
            # msg.data =i
            # pub2.publish(msg)
            
            frame, img = self.camera.read()
            rate.sleep() 
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
                    cv2.putText(img, "2_TWO", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    pub2.publish("2")
                elif (x2 == 1 and x3 == 1 and x4 == 1) and (x1 == 0 and x5 == 0):
                    cv2.putText(img, "3_THREE", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    pub2.publish("3")
                elif (x2 == 1 and x3 == 1 and x4 == 1 and x5 == 1) and (x1 == 0):
                    cv2.putText(img, "4_FOUR", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    pub2.publish("4")
                elif x1 == 1 and x2 == 1 and x3 == 1 and x4 == 1 and x5 == 1:
                    cv2.putText(img, "5_FIVE", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    pub2.publish("5")
                elif x2 == 1 and (x1 == 0, x3 == 0, x4 == 0, x5 == 0):
                    cv2.putText(img, "1_ONE", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    pub2.publish("1")
                elif x1 and (x2 == 0, x3 == 0, x4 == 0, x5 == 0):
                    cv2.putText(img, "GOOD!", (x_1, y_1), cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 3)
                    pub2.publish("good")
            cv2.imshow("camera", img)
            if cv2.getWindowProperty('camera', cv2.WND_PROP_VISIBLE) < 1:
                break
            cv2.waitKey(1)
            # if cv2.waitKey(1) & 0xFF == ord("q"):
        #     break


if __name__ == '__main__':
    Solution = Main()
    Solution.Gesture_recognition()
