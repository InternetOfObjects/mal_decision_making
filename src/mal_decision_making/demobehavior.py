#! coding:utf-8

import sys
import time
import random

import rospy

from std_msgs.msg import String
from mal_msgs.msg import (
    ArmServoMovement,
    LegServoMovement
    )

class Demobehavior(object):

    ARM_SERVO_TOPIC = "/mal_control/control_arm_servo"
    LEG_SERVO_TOPIC = "/mal_control/control_leg_servo"

    def __init__(self, node_name="demobehavior", fps=30):
        rospy.init_node(node_name)
        self.r = rospy.Rate(fps)

        self.arm_pub = rospy.Publisher(self.ARM_SERVO_TOPIC, ArmServoMovement, queue_size=10)
        self.leg_pub = rospy.Publisher(self.LEG_SERVO_TOPIC, LegServoMovement, queue_size=10)
        

    def main(self):

        while not rospy.is_shutdown():


            leg_order = LegServoMovement()
            leg_order.placement = LegServoMovement.PLACE_RIGHT
            leg_order.wise      = LegServoMovement.WISE_RIGHT
            self.leg_pub.publish(leg_order)

            leg_order = LegServoMovement()
            leg_order.placement = LegServoMovement.PLACE_LEFT
            leg_order.wise      = LegServoMovement.WISE_RIGHT
            self.leg_pub.publish(leg_order)

            leg_order = LegServoMovement()
            leg_order.placement = LegServoMovement.PLACE_BACK
            leg_order.wise      = LegServoMovement.WISE_RIGHT
            self.leg_pub.publish(leg_order)

            
            arm_order = ArmServoMovement()
            arm_order.servo_num = random.randint(0, 2)

            movement = random.randint(0, 2)

            if movement == 0:
                arm_order.movement = ArmServoMovement.FORWARD

            if movement == 1:
                arm_order.movement = ArmServoMovement.BACK

            if movement == 2:
                arm_order.movement = ArmServoMovement.STOP

            self.arm_pub.publish(arm_order)
            self.r.sleep()


if __name__ == '__main__':
    dh = Demobehavior()
    dh.main()
