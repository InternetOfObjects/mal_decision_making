#! coding:utf-8

import sys
import time
import random

import rospy

from std_msgs.msg import String
from mal_msgs.msg import (
    ArmServoMovement,
    LegServoMovement,
    Movement
    )

class DemobehaviorArm(object):

    ARM_SERVO_TOPIC = "/mal_control/control_arm_servo"
    LEG_SERVO_TOPIC = "/mal_control/control_leg_servo"
    MOVEMENT_TOPIC = "/mal_control/command"

    def __init__(self, node_name="demobehavior_arm", fps=30):
        rospy.init_node(node_name)
        self.r = rospy.Rate(fps)

        self.arm_pub = rospy.Publisher(self.ARM_SERVO_TOPIC, ArmServoMovement, queue_size=10)
        self.leg_pub = rospy.Publisher(self.LEG_SERVO_TOPIC, LegServoMovement, queue_size=10)
        self.move_pub = rospy.Publisher(self.MOVEMENT_TOPIC, Movement, queue_size=10)
        
    def main(self):

        mov = [Movement.FRONT, Movement.FRONT_LEFT, Movement.FRONT_RIGHT, Movement.BACK, Movement.BACK_LEFT, Movement.BACK_RIGHT, Movement.ROLL_RIGHT, Movement.ROLL_LEFT, Movement.STOP]
        mov_count = 0
        while not rospy.is_shutdown():
            
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
                arm_order.movement = ArmServoMovement.STOP
                self.arm_pub.publish(arm_order)
                
            #self.r.sleep()

            time.sleep(random.randint(0, 3))
            
                
if __name__ == '__main__':
    dh = Demobehavior()
    dh.main()
