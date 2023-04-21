
# imports
from time import sleep, time
#from src.xbox_input import input_loop, ControllerState, controllerState
import threading
#import src.top_controller as TopController
import src.State as State
from src.Config import Configuration
from src.command import Command
import numpy as np
from src.IK import IK
from serial import Serial
import struct
from ctypes import c_float
from math import degrees

# Access to controller and command:
# Controller: xDown(), getCommand(), setButtonCallback(), getLS()
# Command: 
def main():
    # Initializing configuration
    config = Configuration()

    pos1 = 0.1714
    pos2 = -0.03
    pos3 = -0.1883
    # MAIN LOOP #
    while True:
        # Loop to wait for a command
        # print(controllerState.getLS()) # Print Left stick values
        while(True):
            # pos1 = float(input("Pos 1: "))
            # pos2 = float(input("Pos 2: "))
            # pos3 = float(input("Pos 3: "))

            # Don't need identity matrix anymore?
            # T = np.eye(4,dtype=float)
            # T[0,3] = pos1
            # T[1,3] = pos2
            # T[2,3] = pos3

            #ans = IK(0.1714, 0.05, -0.1883, 0, config, 0)
            ans = IK(pos1, pos2, pos3, 0, config, 0)
            print('\nIK Input: ' + str(pos1) + ', ' + str(pos2) + ', ' + str(pos3))
            print('Radians IK output: ' + str(ans))
            c_ans = list(map(c_float,list(map(degrees,ans))))
            
            print('Degrees: ' + str(c_ans))
            print(type(c_ans[1]))


            junk = input('Continue')
            pos2+= 0.01
            if pos2>0.2:
                pos2=0
            # Send out ik anlges to arduino #

            ser = Serial('/dev/cu.usbmodem131488301', 9600, timeout=1)
            # Pack the data into a binary format
            packed_data = struct.pack('4f', *[c.value for c in c_ans])
            # Send the packed data over serial
            ser.write(packed_data)
            print('sent data')




main()
