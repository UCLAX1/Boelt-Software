from Config import Configuration
from IK import IK

config = Configuration()

# config.z_height
# config.x_range
# config.y_range
# config.default_z


def moveFoot(config, legIndex, x, y, z):
    home_pos = config.homePos(legIndex)

    max_z = config.max_z
    min_z = config.default_z

    x_off = choosePercent(config.x_range, x)
    y_off = choosePercent(config.y_range, y)
    z_off = choosePercent([min_z, max_z], z)
    offset = [x_off, y_off, z_off]
    target_pos = home_pos + offset
    q = IK(target_pos, 0, config, legIndex)
    return q


def choosePercent(range, x):
    return (range[1]-range[0])*x
