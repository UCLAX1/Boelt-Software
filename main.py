'''
main.py is the main program runnning on the raspberry pi. It should 
be started as a system process upon bootup.

Here's how it works
1. Main infinite loop: 
    a. defines important config variables and state variables
    b. nested infinite while loop (1/2): 
        - This is for the disabled config
        - Reads xbox values, sees what state the robot should be in (disabled/walking/etc)
        - If no longer disabled, switch to command loop
    c. nested infinite while loop (2/2):
        - This is the command loop
        - commands are sent to robot at a certain sampling rate (dt)
        - Checks to see time since last command, skips interation until at least dt time has passed
        - Does one iteration of stuff
        - Rechecks mode from xbox controller
'''

# imports
from time import sleep, time
from src.xbox.xbox_input import input_loop, ControllerState, controllerState
import threading
import src.top_controller as TopController
import src.State as State
import config as Configuration

def x_test():
    print("X pressed")
def y_test():
    print("Y pressed")
def b_test():
    print("B pressed")
def a_test():
    print("A pressed")

def main():
    thread = threading.Thread(target=input_loop)
    thread.start()
    controllerState.setButtonCallback('x', x_test)
    controllerState.setButtonCallback('y', y_test)
    controllerState.setButtonCallback('b', b_test)
    controllerState.setButtonCallback('a', a_test)
    
    # Create top level controller
    top_controller = TopController()

    #Initializing state
    state = State()

    # Initializing configuration
    config = Configuration()


    # Main Loop
    while True:
        # Loop to wait for a command
        print(controllerState.getLS()) # Print Left stick values
        print("Waiting from command")
        last_loop = time.time()
        while True:
            if JoystickInterface.a_pressed():
                print("A Pressed")
                break
            sleep(0.1)
        # Command Loop
        while True:
            # Run gait controller, based on various inputs
            # Read in controller command
            now = time.time()

            # Check to see if a full cycle time has passed
            if now - last_loop < config.dt:
                # if not, skip this iteration of the loop
                continue
            last_loop = time.time()
            if JoystickInterface.a_pressed():
                break


            
main()
