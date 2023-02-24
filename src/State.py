import numpy as np
from enum import Enum


class State:
    def __init__(self):
        #Took these from pupper, will modify as I understand better
        self.horizontal_velocity = np.array([0.0, 0.0])
        self.activation = 0
        self.behavior_state = BehaviorState.REST

        self.ticks = 0
        self.foot_locations = np.zeros((3, 4))
        self.joint_angles = np.zeros((3, 4))


class BehaviorState(Enum):
    DEACTIVATED = -1
    REST = 0
    TROT = 1
    #Will only get the above three stages working first
    '''
    HOP = 2
    FINISHHOP = 3
    '''
