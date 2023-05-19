import math
import numpy as np
from src.forward_kinematics import forwardKinematics
from src.IK import IK


class Link:
    def __init__(self, L1, d3):
        # Spine to shoulder distance
        self.L1 = L1
        # Shoulder to knee distance
        self.L3 = 99.116E-3
        # Knee to ground distance
        self.L4 = 104E-3
        # Spine top plane to shoulder
        self.d2 = -31.75E-3
        # Shoulder motor axis to center of leg
        self.d3 = d3


class Configuration:
    def __init__(self):
        ######################## GEOMETRY ######################

        # Shoulder motor axis to center of leg
        self._d3_right = 64.008E-3
        self._d3_left = -64.008E-3

        self.center_to_spine = 72.898E-3

        self._x1 = 76.454E-3
        self._y1 = 107.442E-3

        self._x2 = 76.454E-3
        self._y2 = 107.188E-3

        self._L1_rear = math.sqrt(self._x2**2 + self._y2**2)
        self._L1_front = math.sqrt(self._x1**2 + self._y1**2)

        ################### LINKS ###################
        self._fr = Link(self._L1_front, self._d3_right)
        self._fl = Link(self._L1_front, self._d3_left)
        self._bl = Link(self._L1_rear, self._d3_left)
        self._br = Link(self._L1_rear, self._d3_right)

        ################### Offsets ###################
        self._t1 = math.atan2(self._x1, self._y1)
        self._t2 = math.atan2(self._x2, self._y2)
        self._off_fr = np.array([self._t1, math.pi/2-self._t1, -math.pi/2, 0])
        self._off_fl = np.array([math.pi-self._t1, self._t1-math.pi/2, -math.pi/2, 0])
        self._off_bl = np.array([self._t2-math.pi, -math.pi/2-self._t2, -math.pi/2, 0])
        self._off_br = np.array([-self._t2, self._t2+math.pi/2, -math.pi/2, 0])

        #################### GAIT #######################
        self.dt = 0.01
        self.num_phases = 4
        self.contact_phases = np.array(
            [[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1], [
                0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
        )

        self.overlap_time = 0.10  # duration of the phase where all four feet are on the ground
        self.swing_time = 0.15  # duration of the phase when only two feet are on the ground

        #################### DEFAULT STANCE #######################
        self.default_z = -0.1883
        self.x_range = np.array([-0.04, 0.04])
        self.y_range = np.array([-0.04, 0.04])
        self.z_height = 0.05

    def offset(self, legIndex):
        match legIndex:
            case 0:
                return self._off_fr
            case 1:
                return self._off_fl
            case 2:
                return self._off_bl
            case 3:
                return self._off_br

    def link(self, legIndex):
        match legIndex:
            case 0:
                return self._fr
            case 1:
                return self._fl
            case 2:
                return self._bl
            case 3:
                return self._br

    def getDH(self, leg_index):
        links = self.link(leg_index)
        DH = dict()
        DH["alpha"] = np.array([0, 0, np.pi/2, 0, 0])
        DH["a"] = np.array([0, links.L1, 0, links.L3, links.L4])
        DH["d"] = np.array([0, links.d2, links.d3, 0, 0])
        return DH

    def convertAngles(self, joints, leg_index):
        return joints+self.offset(leg_index)

    def fkine(self, joints, leg_index):
        DH = self.getDH(leg_index)
        q = self.convertAngles(joints, leg_index)
        q2 = np.append(q, 0)
        T = forwardKinematics(
            a=DH["a"], alpha=DH["alpha"], d=DH["d"], theta=q2)
        pos = T[0:3, 3]
        return pos

    def homePos(self, leg_index):
        ans = self.fkine(np.zeros(4), leg_index)
        ans[2] = self.default_z
        return ans
