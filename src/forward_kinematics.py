import numpy as np
from numpy import sin, cos, pi
from functools import reduce


def oneFrameFkine(a, alpha, d, theta):
    T = np.array([
        [cos(theta), -sin(theta), 0, a],
        [sin(theta)*cos(alpha), cos(theta) *
         cos(alpha), -sin(alpha), -sin(alpha)*d],
        [sin(theta)*sin(alpha), cos(theta) *
         sin(alpha), cos(alpha), cos(alpha)*d],
        [0, 0, 0, 1]
    ])
    return T


def forwardKinematics(a, alpha, d, theta):
    Ts = map(oneFrameFkine, a, alpha, d, theta)
    T = reduce(np.matmul, Ts)
    return T


# config = Configuration()
# config.fkine([0, 0, 0, 0], 0)
