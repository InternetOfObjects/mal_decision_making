#! coding:utf-8

import sys
import time

import rospy

from std_msgs.msg import String
from mal_msgs.msg import ArmServoMovement

class Demobehavior(object):

    ARM_SERVO_TOPIC = "/mal_control/control_arm_servo"

    def __init__(self, node_name="demobehavior", fps=30):
        rospy.init_node(node_name)
        self.r = rospy.Rate(fps)

        self.pub = rospy.Publisher(self.ARM_SERVO_TOPIC, ArmServoMovement, queue_size=10)

    def main(self):

        while not rospy.is_shutdown():

            order = ArmServoMovement()
            order.servo_num = 2
            order.movement = ArmServoMovement.FORWARD

            print order

            self.pub.publish(order)
            self.r.sleep()


if __name__ == '__main__':
    dh = Demobehavior()
    dh.main()
