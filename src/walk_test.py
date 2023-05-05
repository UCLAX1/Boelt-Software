#Phase 1:
#
#   leg 4:
#    forward by one workspace length
#
#    leg 2:
#    forward by one workspace length
#
#    body motion:
#    all four legs move back in stance by half a workspace length
#
#Phase 2:
#
#    leg 3:
#    forward by one workspace length
#    leg 1
#    forward by one workspace length

import move_foot as mf
from Config import Configuration


config = Configuration()

def leg_forward(leg, distance):
    for i in range(0.0, distance + 0.01, 0.01):
        if(i <= distance / 2):
            mf.moveFoot(config, leg, i, i, i)
        else:
            mf.moveFoot(config, leg, i, 1.0-i, i)
    print(f"Leg {leg}: Forward by {distance} workspace length")

def body_motion(distance):
    print(f"Body motion: All four legs move back in stance by {distance} workspace length")

def walking():
    # Phase 1
    leg_forward(4, 1)  # Leg 4 forward by one workspace length
    leg_forward(2, 1)  # Leg 2 forward by one workspace length
    body_motion(0.5)   # Body motion

    # Phase 2
    leg_forward(3, 1)  # Leg 3 forward by one workspace length
    leg_forward(1, 1)  # Leg 1 forward by one workspace length

walking()

    
