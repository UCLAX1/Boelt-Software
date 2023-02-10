from evdev import list_devices, InputDevice, categorize, ecodes, KeyEvent
import time

# CONSTANTS
THRESHOLD = 3000

#  GET INPUT EVENTS FROM DEVICES
calibrated = False
centers = [1000, 1000, 1000, 1000]
devices = [InputDevice(path) for path in list_devices()]
controller = None
for device in devices:
    # # print devides to check which is the controller
    #     print(device.path, device.name, device.phys)
    # Set Controller to the device that contains the phrase X-Box
    if ("X-Box" in device.name):
        controller = device


#######################
#### EVENT READING ####
#######################
for event in controller.read_loop():
    keyevent = categorize(event)

#### BUTTONS
    if (event.type == ecodes.EV_KEY):
        print(keyevent.keycode)
        #Detecting down presses only

        #X
        if (keyevent.keycode[0] == 'BTN_NORTH' and keyevent.keystate == KeyEvent.key_down):
            print('X')
        #A
        if (keyevent.keycode[0] == 'BTN_A' and keyevent.keystate == KeyEvent.key_down):
            print('A')
        #Y
        if (keyevent.keycode[0] == 'BTN_WEST' and keyevent.keystate == KeyEvent.key_down):
            print('Y')
        #B
        if (keyevent.keycode[0] == 'BTN_B' and keyevent.keystate == KeyEvent.key_down):
            print('B')

#### JOYSTICKS
    elif (event.type == ecodes.EV_ABS):
        #print(str(keyevent) + " code: " + str(event.code))
        val = event.value
        # Ensure it's above threshold
        if(abs(val) < THRESHOLD):
            val = 0
        
        #### NEED TO DOUBLE CHECK DIRECTIONS AND SIGN FLIPS
        # Left Stick X
        if (event.code == 0 and val > 0):
            print(f'LS Right: {val}')
        if (event.code == 0 and val < 0):
            print(f'LS Left: {val}')
        # Left Stick Y (Signs are backwards from intuition)
        if (event.code == 1 and val > 0):
            print(f'LS Backward: {val}')
        if (event.code == 1 and val < 0):
            print(f'LS Forward: {val}')
        # Left Stick X
        if (event.code == 3 and val > 0):
            print(f'RS Right: {val}')
        if (event.code == 3 and val < 0):
            print(f'RS Left: {val}')
        # Left Stick Y (Signs are backwards from intuition)
        if (event.code == 4 and val > 0):
            print(f'RS Backward: {val}')
        if (event.code == 4 and val < 0):
            print(f'RS Forward: {val}')

