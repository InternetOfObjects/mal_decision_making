#!/usr/bin/env python

import rospy

from mal_decision_making import DemobehaviorArm

if __name__ == '__main__':
    try:
        node = DemobehaviorArm()
        node.main()
    except rospy.ROSInterruptException:
        pass
