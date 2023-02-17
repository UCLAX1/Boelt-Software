from evdev import list_devices, InputDevice, categorize, ecodes, KeyEvent
import time
import threading

# CONSTANTS


class ControllerState:
    THRESHOLD = 5000
    CENTERS = {"LS_Y": 1000, "LS_X": 2000, "RS_Y": 1000, "RS_X": 1000}

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

    #####################
    ## UPDATE FUNCTION ##
    #####################

    def setButtonCallback_X(self, button, func):
        if button == 'x':
            self.callback_x = func
        elif button == 'y':
            self.callback_y = func
        elif button == 'b':
            self.callback_b = func
        elif button == 'a':
            self.callback_a = func

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

# JOYSTICKS
        elif (event.type == ecodes.EV_ABS):
            # print(str(keyevent) + " code: " + str(event.code))
            val = event.value
            # Ensure it's above threshold
            
            # NEED TO DOUBLE CHECK DIRECTIONS AND SIGN FLIPS
            # Left Stick X
            if (event.code == 0):
                # Testing centers for actual code put this at end of this if
                if (not(val-self.CENTERS["LS_X"] > self.THRESHOLD or val+self.CENTERS["LS_X"] < -self.THRESHOLD)):
                    val = 0
                self.ls_state[0] = val
            # Left Stick Y (Signs are backwards from intuition)
            if (event.code == 1):
                if (not(val-self.CENTERS["LS_Y"] > self.THRESHOLD or val+self.CENTERS["LS_Y"] < -self.THRESHOLD)):
                    val = 0
                self.ls_state[1] = -val

            # # Right Stick X
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
    # If there is more logic, add below

    def getLS(self):
        return self.ls_state

#######################
#### EVENT READING ####
#######################
controllerState = ControllerState()


def input_loop():
    global controllerState
    for event in controllerState.controller.read_loop():
        controllerState.update(event)


# In the file where you want to use xbox_input:


