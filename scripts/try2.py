import numpy as np
import rospy
from sensor_msgs.msg import JointState


def callback(msg):
    arr=np.array(msg.position)
    print(arr[1])
if __name__ == "__main__":
    rospy.init_node('made')
    sub = rospy.Subscriber("joint_states",JointState,callback,queue_size=10)
    rospy.spin()