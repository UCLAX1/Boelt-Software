import numpy as np
from enum import Enum, IntEnum


class State:
    def __init__(self):
        self.horizontal_velocity = np.array([0.0, 0.0])
        self.activation = 0
        self.behavior_state = BehaviorState.REST

        self.ticks = 0
        self.foot_locations = np.zeros((3, 4))
        self.joint_angles = np.zeros((3, 4))
        self.spine_angles = np.zeros((1,2))


class BehaviorState(Enum):
    DEACTIVATED = -1
    REST = 0
    WALK = 1

class LEG_INDEX(IntEnum):
    FR = 0
    FL = 1
    BL = 2
    BR = 3