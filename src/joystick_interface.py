from evdev import list_devices, InputDevice, categorize, ecodes, KeyEvent
import time
import threading

##### This class lets you read the controller by  #####
##### letting input loop run in a separate thread #####
# Global controllerState variable
# Public functions: getLS(), setButtonCallback(buttonLetter, func), input_loop()

# Todo: Right Stick, top buttons, get button down, simple directional checks?

class ControllerState:
    THRESHOLD = 5000
    # Default centers of sticks. To test values, disable the val=0 code for joysticks
    CENTERS = {"LS_Y": 1000, "LS_X": 2000, "RS_Y": 1000, "RS_X": 1000}

    # Initialize controller and instance variables
    def __init__(self):
        self.devices = [InputDevice(path) for path in list_devices()]
        self.controller = None
        for device in self.devices:
            # # print devides to check which is the controller
            #     print(device.path, device.name, device.phys)
            # Set Controller to the device that contains the phrase X-Box
            if ("X-Box" in device.name):
                self.controller = device
        self.joysticks = {"ls_x": 0, "ls_y": 0, "rs_x": 0, "rs_y": 0}

        self.ls_state = [0,0]
        self.rs_state = [0,0]

        self.callback_x = None
        self.callback_y = None
        self.callback_b = None
        self.callback_a = None

        self.x_down = False
        self.y_down = False
        self.b_down = False
        self.a_down = False

    def xDown(self):
        return self.a_down 
    def yDown(self):
        return self.y_down 
    def bDown(self):
        return self.b_down 
    def aDown(self):
        return self.a_down 

    #####################
    ## UPDATE FUNCTION ##
    #####################

    # Allows external files to set a callback function for buttons to call
    def setButtonCallback_X(self, button, func):
        if button == 'x':
            self.callback_x = func
        elif button == 'y':
            self.callback_y = func
        elif button == 'b':
            self.callback_b = func
        elif button == 'a':
            self.callback_a = a_pressed

    # Takes an event and updates instance variables and calls respective callbacks
    def update(self, event):
        keyevent = categorize(event)
        # UPDATE  BUTTONS
        if (event.type == ecodes.EV_KEY):
            print(keyevent.keycode)
            # Detecting down presses only
            # X
            if (keyevent.keycode[0] == 'BTN_NORTH' and keyevent.keystate == KeyEvent.key_down):
                self.x_down = True if keyevent.keystate == KeyEvent.key_down else False
                if (self.callback_x):
                    self.callback_x()
            # A
            if (keyevent.keycode[0] == 'BTN_A' and keyevent.keystate == KeyEvent.key_down):
                self.a_down = True if keyevent.keystate == KeyEvent.key_down else False
                if (self.callback_a):
                    self.callback_a()
            # Y
            if (keyevent.keycode[0] == 'BTN_WEST' and keyevent.keystate == KeyEvent.key_down):
                self.y_down = True if keyevent.keystate == KeyEvent.key_down else False
                if (self.callback_y):
                    self.callback_y()
            # B
            if (keyevent.keycode[0] == 'BTN_B' and keyevent.keystate == KeyEvent.key_down):
                self.b_down = True if keyevent.keystate == KeyEvent.key_down else False
                if (self.callback_b):
                    self.callback_b()
            # A up
            if (keyevent.keycode[0] == 'BTN_A' and keyevent.keystate == KeyEvent.key_up):
                self.a_down = False if keyevent.keystate == KeyEvent.key_up else True

# JOYSTICKS
        elif (event.type == ecodes.EV_ABS):
            # print(str(keyevent) + " code: " + str(event.code))
            val = event.value
            
            # Left Stick X
            if (event.code == 0):
                if (not(val-self.CENTERS["LS_X"] > self.THRESHOLD or val+self.CENTERS["LS_X"] < -self.THRESHOLD)):
                    val = 0
                self.ls_state[0] = val
            # Left Stick Y (Signs are naturally backwards from intuition, but is changed to be standard cartesian here)
            if (event.code == 1):
                if (not(val-self.CENTERS["LS_Y"] > self.THRESHOLD or val+self.CENTERS["LS_Y"] < -self.THRESHOLD)):
                    val = 0
                self.ls_state[1] = -val

            # # Right Stick X not implemented yet
            # if (event.code == 3):
            #     if (val-self.CENTERS["RS_X"] > self.THRESHOLD):
            #         #print(f'RS Right: {val}')
            #         pass
            #     if (val+self.CENTERS["RS_X"] < self.THRESHOLD):
            #         #print(f'RS Right: {val}')
            #         pass
            # # Right Stick Y (Signs are backwards from intuition)
            # if (event.code == 4):
            #     if (val-self.CENTERS["RS_Y"] > self.THRESHOLD):
            #         #print(f'RS Backward: {val}')
            #         pass
            #     if (val+self.CENTERS["RS_Y"] < self.THRESHOLD):
            #         #print(f'RS Forward: {val}')
            #         pass
    # If there is more logic, add below (i.e. set diagonal? set quadrant/octant status of sticks?)

    def getLS(self):
        return self.ls_state

#######################
#### EVENT READING ####
#######################

# Initialize controllerState
controllerState = ControllerState()

# Create a public getter functions for each button
def a_pressed():
    return controllerState.aDown()
def b_pressed():
    return controllerState.bDown()
def x_pressed():
    return controllerState.xDown()
def y_pressed():
    return controllerState.yDown()

# Create global variable and enter event loop
# - Must be run in separate thread
def input_loop():
    global controllerState
    for event in controllerState.controller.read_loop():
        controllerState.update(event)


# In the file where you want to use xbox_input:

