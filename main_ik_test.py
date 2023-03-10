
# imports
from time import sleep, time
from src.xbox_input import input_loop, ControllerState, controllerState
import threading
import src.top_controller as TopController
import src.State as State
import config as Configuration
from src.command import Command
import numpy as np
import IK


# Access to controller and command:
# Controller: xDown(), getCommand(), setButtonCallback(), getLS()
# Command: 
def main():
    # Initializing configuration
    config = Configuration()


    # MAIN LOOP #
    while True:
        # Loop to wait for a command
        # print(controllerState.getLS()) # Print Left stick values
        while(True):
            pos1 = int(input("Pos 1: "))
            pos2 = int(input("Pos 2: "))
            pos3 = int(input("Pos 3: "))

            T = np.eye(4,dtype=float)
            T[0,3] = pos1
            T[1,3] = pos2
            T[2,3] = pos3
            
            ik_angles = IK(config, T, 0, 0)

            #send out ik anlges to arduino


main()
