import numpy as np
from transforms3d.euler import euler2mat

class StanceController:
    #initialize physical parameters from config
    def __init__(self, config):
        self.config = config

    #calculates the difference in position. delta_p is the linear movement from the command velocity,
    #and delta_R is the rotation matrix from the command change in yaw (if turning is needed)
    def position_delta(self, leg_index, state, command):

        delta_x = -command.horizontal_velocity[0] * self.config.dt
        delta_y = -command.horizontal_velocity[1] * self.config.dt

        #z location of the foot, moves the foot up/down only if state.height is different from current
        #value of z. z movement velocity is determined by self.config.z_time_constant.
        z = state.foot_locations[2, leg_index]
        delta_z = (1.0 / self.config.z_time_constant) * (state.height - z) * self.config.dt

        delta_R = euler2mat(0, 0, -command.yaw_rate * self.config.dt)
        delta_p = np.array((delta_x, delta_y, delta_z))
        return (delta_p, delta_R)

    #main function. called from main controller to get the change in location of a leg in stance state.
    #state is an object containing the coordinates of the feet (state.foot_locations), and the height,
    #and command is an object containing the desired forward velocity, and the desired yaw rate (turning speed)
    def next_foot_location(self, leg_index, state, command):
        foot_location = state.foot_locations[:, leg_index]
        (delta_p, delta_R) = self.position_delta(leg_index, state, command)
        incremented_location = delta_R @ foot_location + delta_p

        return incremented_location