#!/usr/bin/env python

import rospy

from mal_decision_making import LocalController

if __name__ == '__main__':
    try:
        node = LocalController()
        node.main()
    except rospy.ROSInterruptException:
        pass
