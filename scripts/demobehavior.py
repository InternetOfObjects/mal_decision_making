#!/usr/bin/env python

import rospy

from mal_decision_making import Demobehavior

if __name__ == '__main__':
    try:
        node = Demobehavior()
        node.main()
    except rospy.ROSInterruptException:
        pass
