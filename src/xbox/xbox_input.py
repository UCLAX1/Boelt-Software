from evdev import list_devices, InputDevice, categorize, ecodes, KeyEvent
import time

# CONSTANTS
vertical_threshold = 2000
horizontal_threshold = 2000

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


# Process all events
for event in controller.read_loop():
    keyevent = categorize(event)

#     Read Button Presses
    if (event.type == ecodes.EV_KEY):
        print(keyevent.keycode)
#         Detecting down presses only

#       X
        if (keyevent.keycode[0] == 'BTN_NORTH' and keyevent.keystate == KeyEvent.key_down):
            print('X')
#       A
        if (keyevent.keycode[0] == 'BTN_A' and keyevent.keystate == KeyEvent.key_down):
            print('A')
#       Y
        if (keyevent.keycode[0] == 'BTN_WEST' and keyevent.keystate == KeyEvent.key_down):
            print('Y')
            if (calibrated == False):

                #       B
        if (keyevent.keycode[0] == 'BTN_B' and keyevent.keystate == KeyEvent.key_down):
            print('B')

    elif (event.type == ecodes.EV_ABS):
        val = event.value
        if (event.code == 1):
            val = -val
            print(f'Left Stick Y: {val}')
            if (val >= vertical_threshold):
                print('left forward')
#         print(str(keyevent) + " code: " + str(event.code))
#         if(event.code ==0):
#             print(f'Left Stick X: {val}')
#         if(event.code ==3):
#             print(f'Right Stick X: {val}')
#         if(event.code ==4):
#             print(f'Right Stick Y: {val}')

        pass
