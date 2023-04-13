from IK import IK
import numpy as np
from Config import Configuration

C = Configuration()
T = np.identity(4)
T[0:3,3] = [0.17, 0.076, -0.2]
Q = IK(C,T, 0, 0)
print(Q)