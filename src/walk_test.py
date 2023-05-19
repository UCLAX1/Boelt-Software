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

def leg_motion(leg, startingPercent, endingPercent, increment, currentPos):
    startingPercent = int(startingPercent * 100)
    endingPercent = int(endingPercent * 100)
    distance = (endingPercent - startingPercent) / 2
    rateOfGrowth = 100/distance
    zCount = 0.0
    for i in range(startingPercent, endingPercent + increment, increment):
        if(i < (startingPercent + distance)): #if not at halfway point
            currentPos[leg] = mf.moveFoot(config, leg, 0.5, i /100, zCount)
            zCount = zCount + (increment * rateOfGrowth) / 100 #z should be growing at a faster rate to get to 1 at the halfway
        else:
            currentPos[leg] = mf.moveFoot(config, leg, 0.5, i/100, zCount)
            zCount = zCount - (increment * rateOfGrowth) / 100 #z should go back down to 0 in the second half of the traversal
        for i, value in enumerate(currentPos):
            print(f"Index {i}: {value}")
    print(f"Leg {leg}: Moved from {startingPercent} to {endingPercent}")

def body_motion(distance, positions, increment, currentPos):
    distance = int(distance * 100)
    for i in range(0, distance + increment, increment):
        currentPos[0] = mf.moveFoot(config, 0, 0.5, positions[0] - i, 0.0)
        currentPos[1] = mf.moveFoot(config, 1, 0.5, positions[1] - i, 0.0)
        currentPos[2] = mf.moveFoot(config, 2, 0.5, positions[2] - i, 0.0)
        currentPos[3] = mf.moveFoot(config, 3, 0.5, positions[3] - i, 0.0)
    print(f"Body motion: All four legs move back in stance by {distance} workspace length")

def startup(increment, currentPos):
    #Assume stable (all legs at 0.5) 
    leg_motion(2, 0.5, 1.0, increment, currentPos) # Leg 2 forward from 0.5 to 1.0
    leg_motion(1, 0.5, 1.0, increment, currentPos) # Leg 1 forward from 0.5 to 1.0 
    body_motion(0.5, [0.5,1.0,1.0,0.5], increment, currentPos) # move body forward to normalize legs 2 and 1 to 0.5 
                                        # legs 0 and 3 are at 0
def phase1(increment, currentPos):
 # Now legs are in position to begin Phase 1
    leg_motion(3, 0.5, 1.0, increment, currentPos)  # Leg 3 forward by one workspace length
    leg_motion(0, 0.5, 1.0, increment, currentPos)  # Leg 0 forward by one workspace length
    #body_motion(0.5, [1.0,0.5,0.5,1.0], increment, currentPos)  # move body forward to normalize legs 3 and 0 to 0.5 
                                         # legs 2 and 1 are at 0

def phase2(increment, currentPos):
# Now legs are in position to begin Phase 2
    leg_motion(2, 0.0, 1.0, increment, currentPos)  # Leg 2 forward by one workspace length
    leg_motion(2, 0.0, 1.0, increment, currentPos)  # Leg 1 forward by one workspace length
    body_motion(0.5, [0.5,1.0,1.0,0.5], increment, currentPos)  # move body forward to normalize legs 2 and 1 to 0.5 
                                         # legs 0 and 3 are at 0
def walking(increment, currentPos):
    phase1(increment, currentPos)


    
