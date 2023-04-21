import numpy as np

class StanceController:
    def __init__(self, config):
        self.config = config

    def position_delta(self, leg_index, state, command):
        """
        Calculate the difference between the next desired body location and the current body location
        Returns position increment 
        """
        z = state.foot_locations[2, leg_index] # z coord of foot relative to body
        v_xy = np.array( 
            [
                -command.horizontal_velocity[0],
                -command.horizontal_velocity[1],
                0 # zero bc boelt not moving up and down; maybe change later
            ]
        )
        delta_p = v_xy * self.config.dt # distance = velocity * time 
        return delta_p

    def next_foot_location(self, leg_index, state, command):
        """
        Returns new position
        """
        foot_location = state.foot_locations[:, leg_index] # xyz of foot pos.
        delta_p = self.position_delta(leg_index, state, command)
        incremented_location = foot_location + delta_p

        return incremented_location