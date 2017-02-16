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

class LocalController(object):

    ARM_SERVO_TOPIC = "/mal_control/control_arm_servo"
    LEG_SERVO_TOPIC = "/mal_control/control_leg_servo"
    MOVEMENT_TOPIC = "/mal_control/command"

    def __init__(self, node_name="local_controller", fps=30):
        rospy.init_node(node_name)
        self.r = rospy.Rate(fps)

        self.arm_pub = rospy.Publisher(self.ARM_SERVO_TOPIC, ArmServoMovement, queue_size=10)
        self.leg_pub = rospy.Publisher(self.LEG_SERVO_TOPIC, LegServoMovement, queue_size=10)
        self.move_pub = rospy.Publisher(self.MOVEMENT_TOPIC, Movement, queue_size=10)
        
    def main(self):

        mov = [Movement.FRONT, Movement.FRONT_LEFT, Movement.FRONT_RIGHT, Movement.BACK, Movement.BACK_LEFT, Movement.BACK_RIGHT, Movement.ROLL_RIGHT, Movement.ROLL_LEFT, Movement.STOP]
        mov_count = 0 
        mov_duration = 500
        while not rospy.is_shutdown():

            print "plz type of direction"
            mov_count = int(raw_input())
            print "plz type of duration"
            mov_duration = int(raw_input())

            print "Current Movement : " + str(mov_count)
            
            movement = Movement()
            movement.movement = mov[mov_count]
            movement.duration = mov_duration / 1000.0
            self.move_pub.publish(movement)

            time.sleep(1)

                
if __name__ == '__main__':
    dh = Demobehavior()
    dh.main()
