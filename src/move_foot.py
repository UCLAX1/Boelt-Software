from Config import Configuration
from IK import IK

config = Configuration()

# config.z_height
# config.x_range
# config.y_range
# config.default_z


def moveFoot(config, legIndex, x, y, z):
    home_pos = config.homePos(legIndex)
    x_off = choosePercent(config.x_range, x)
    y_off = choosePercent(config.y_range, y)
    z_off = config.default_z

    offset = [x_off, y_off, z_off]
    target_pos = home_pos + offset
    IK(target_pos, 0, config, legIndex)


def choosePercent(range, x):
    return (range[1]-range[0])*x