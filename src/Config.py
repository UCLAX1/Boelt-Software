import math


class Configuration:
    def __init__(self):
       
        ######################## GEOMETRY ######################
        # Shoulder to knee distance
        self.L3 = 72.75E-3

        # Knee to ground distance
        self.L4 = 130.57E-3

        # Smath.pine top plane to shoulder
        self.d2 = -31.75E-3

        # Shoulder motor axis to center of leg
        self.d3= 64.008E-3

        self.center_to_spine = 72.898E-3

        self.x1 = 76.454E-3
        self.y1 = 107.442E-3

        self.x2 = 76.454E-3
        self.y2 = 107.188E-3

        self.L1__rear = math.sqrt(self.x2**2 + self.y2**2)
        self.L1_front = math.sqrt(self.x1**2 + self.y1**2)


def fr(t1):
    off1 = t1
    off2 = math.pi/2-t1
    off3 = -math.pi/2


def fl(t1):
    off1 = math.pi-t1
    off2 = t1-math.pi/2
    off3 = -math.pi/2


def br(t2):
    off1 = -t2
    off2 = t2+math.pi/2
    off3 = -math.pi/2


def off = bl(t2):
    off1 = t2-math.pi
    off2 = -math.pi/2-t2
    off3 = -math.pi/2
