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
            isMoveLeg = random.randint(0, 100)

            placement_randomize = random.randint(0, 2)
            wise_randomize = random.randint(0, 2)

            leg_stopped = True

            if isMoveLeg < 50:

                num_of_place = random.randint(1, 3)

                for i in xrange(0, num_of_place):

                    if placement_randomize == 0:
                        leg_order.placement = LegServoMovement.PLACE_RIGHT

                    if placement_randomize == 1:
                        leg_order.placement = LegServoMovement.PLACE_LEFT

                    if placement_randomize == 2:
                        leg_order.placement = LegServoMovement.PLACE_BACK

                    if wise_randomize == 0:
                        leg_order.wise      = LegServoMovement.WISE_RIGHT

                    if wise_randomize == 1:
                        leg_order.wise      = LegServoMovement.WISE_LEFT

                    if wise_randomize == 2:
                        leg_order.wise      = LegServoMovement.WISE_STOP

                    rospy.loginfo("==================== Base Moving")
                    rospy.loginfo(leg_order)

                    self.leg_pub.publish(leg_order)

            else:
                rospy.loginfo("==================== Base Stop")

                leg_order.placement = LegServoMovement.PLACE_RIGHT
                leg_order.wise      = LegServoMovement.WISE_STOP
                self.leg_pub.publish(leg_order)


                leg_order.placement = LegServoMovement.PLACE_LEFT
                leg_order.wise      = LegServoMovement.WISE_STOP
                self.leg_pub.publish(leg_order)

                leg_order.placement = LegServoMovement.PLACE_BACK
                leg_order.wise      = LegServoMovement.WISE_STOP
                self.leg_pub.publish(leg_order)

                #leg_stopped = True
                

            arm_order = ArmServoMovement()
            isMoveArm = random.randint(0, 100)
            if isMoveArm < 100:

                rospy.loginfo("==================== Arm Moving")
                arm_order.servo_num = random.randint(0, 2)

                movement = random.randint(0, 2)

                if movement == 0:
                    arm_order.movement = ArmServoMovement.FORWARD

                if movement == 1:
                    arm_order.movement = ArmServoMovement.BACK

                if movement == 2:
                    arm_order.movement = ArmServoMovement.STOP

                rospy.loginfo(arm_order)

                self.arm_pub.publish(arm_order)
                self.r.sleep()
            else:
                rospy.loginfo("==================== Arm Stopping")
                arm_order.movement = ArmServoMovement.STOP
                self.arm_pub.publish(arm_order)
                
            #self.r.sleep()

            time.sleep(random.randint(0, 3))
                


if __name__ == '__main__':
    dh = Demobehavior()
    dh.main()
