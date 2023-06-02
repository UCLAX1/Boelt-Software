from Config import Configuration
from IK import IK
import numpy as np

config = Configuration()

# config.z_height
# config.x_range
# config.y_range
# config.default_z


def moveFoot(config, legIndex, x, y, z):
    home_pos = config.homePos(legIndex)

    min_z = config.default_z
    max_z = config.z_height + min_z

    x_off = choosePercent(config.x_range, x)
    y_off = choosePercent(config.y_range, y)
    z_off = choosePercent([min_z, max_z], z)
    offset = [x_off, y_off, z_off]
    home_pos[2] = 0
    target = home_pos + offset
    print(target)
    q = IK(target, 0, config, legIndex)
    print(f"Actual Location {config.fkine(q, legIndex)}")
    print(f"Target:         {target}")
    return q


def choosePercent(range, x):
    return (range[1]-range[0])*x + range[0]


# q = moveFoot(config, 0, 0.5, 0.5, 0)


def moveTest(config):
    vals = np.zeros((4, 11))
    for leg_index in range(4):
        print(f"Leg index: {leg_index}")
        for y in range(11):
            y_val = y/10
            print(f"leg {leg_index} and position {y}")
            q = moveFoot(config, leg_index, 0.5, y_val, 0)
            ans = config.fkine(q, leg_index)
            vals[leg_index, y] = ans[1]
    print(vals)
    return vals
