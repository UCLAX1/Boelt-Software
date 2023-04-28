import numpy as np
from config import Configuration

config = Configuration()


# The right and left legs have different values for d3 (negative and positive)
d_right = np.array([0, config._d2, config.d3, 0, 0])
d_left = np.array([0, config._d2, -config.d3, 0, 0])

def getDH(config, leg_index):
    links = config.link(leg_index)
    DH = dict()
    DH["alpha"] = np.array([0, 0, np.pi/2, 0, 0])
    DH["a"] = np.array([0, links.L1, 0, config.L3, config.L4])
    DH["d"] = np.array([0, links.d2, links.d3, 0, 0])





