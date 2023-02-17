from evdev import list_devices, InputDevice, categorize, ecodes, KeyEvent
import time
import threading

# CONSTANTS


class ControllerState:
    THRESHOLD = 3000
    CENTERS = {"LS_Y": 1000, "LS_X": 1000, "RS_Y": 1000, "RS_X": 1000}

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
        self.callback_x = None

    #####################
    ## UPDATE FUNCTION ##
    #####################

    def setCallback_X(self, func):
        self.callback_x = func

    def update(self, event):
        keyevent = categorize(event)
        # UPDATE  BUTTONS
        if (event.type == ecodes.EV_KEY):
            print(keyevent.keycode)
            # Detecting down presses only
            # X
            if (keyevent.keycode[0] == 'BTN_NORTH' and keyevent.keystate == KeyEvent.key_down):
                if (self.callback_x):
                    self.callback_x()
            # A
            if (keyevent.keycode[0] == 'BTN_A' and keyevent.keystate == KeyEvent.key_down):
                print('A')
            # Y
            if (keyevent.keycode[0] == 'BTN_WEST' and keyevent.keystate == KeyEvent.key_down):
                print('Y')
            # B
            if (keyevent.keycode[0] == 'BTN_B' and keyevent.keystate == KeyEvent.key_down):
                print('B')

# JOYSTICKS
        elif (event.type == ecodes.EV_ABS):
            # print(str(keyevent) + " code: " + str(event.code))
            val = event.value
            # Ensure it's above threshold
            if (abs(val) < self.THRESHOLD):
                val = 0

            # NEED TO DOUBLE CHECK DIRECTIONS AND SIGN FLIPS
            # Left Stick X
            if (event.code == 0):
                if (val-self.CENTERS["LS_X"] > self.THRESHOLD):
                    print(f'LS Right: {val}')
                if (val+self.CENTERS["LS_X"] < self.THRESHOLD):
                    print(f'LS Right: {val}')
            # Faster version: (Don't know if it matters, little difference)
            # if (event.code == 0 and val > 0):
            #     print(f'LS Right: {val}')
            # elif (event.code == 0 and val < 0):
            #     print(f'LS Left: {val}')

            # Left Stick Y (Signs are backwards from intuition)
            if (event.code == 1):
                if (val-self.CENTERS["LS_Y"] > self.THRESHOLD):
                    print(f'LS Backward: {val}')
                if (val+self.CENTERS["LS_Y"] < self.THRESHOLD):
                    print(f'LS Forward: {val}')

            # Right Stick X
            if (event.code == 3):
                if (val-self.CENTERS["RS_X"] > self.THRESHOLD):
                    print(f'RS Right: {val}')
                if (val+self.CENTERS["RS_X"] < self.THRESHOLD):
                    print(f'RS Right: {val}')
            # Right Stick Y (Signs are backwards from intuition)
            if (event.code == 4):
                if (val-self.CENTERS["RS_Y"] > self.THRESHOLD):
                    print(f'RS Backward: {val}')
                if (val+self.CENTERS["RS_Y"] < self.THRESHOLD):
                    print(f'RS Forward: {val}')


#######################
#### EVENT READING ####
#######################
controllerState = ControllerState()


def input_loop():
    global controllerState
    for event in controllerState.controller.read_loop():
        controllerState.update(event)


# In the file where you want to use xbox_input:
