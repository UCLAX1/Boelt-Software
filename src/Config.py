import math
import numpy as np


class Link:
    def _init_(self, L1, d3): 
        # Spine to shoulder distance
        self.L1 = L1
        # Shoulder to knee distance
        self.L3 = 72.75E-3
        # Knee to ground distance
        self.L4 = 130.57E-3
         # Spine top plane to shoulder
        self.d2 = -31.75E-3
        # Shoulder motor axis to center of leg
        self.d3 = d3       


class Configuration:
    def _init_(self):
       
        ######################## GEOMETRY ######################
        
        # Shoulder motor axis to center of leg
        self._d3_right= 64.008E-3
        self._d3_left = -64.008E-3

        self.center_to_spine = 72.898E-3

        self._x1 = 76.454E-3
        self._y1 = 107.442E-3

        self._x2 = 76.454E-3
        self._y2 = 107.188E-3

        self._L1_rear = math.sqrt(self.x2**2 + self.y2**2)
        self._L1_front = math.sqrt(self.x1**2 + self.y1**2)

        ################### LINKS ###################
        self._fr = Link(self._L1_front, self._d3_right)
        self._fl = Link(self._L1_front, self._d3_left)
        self._bl = Link(self._L1_rear, self._d3_left)
        self._br = Link(self._L1_rear, self._d3_right)

        ################### Offsets ###################       
        self._t1 = math.atan2(self._x1,self._y1)
        self._t2 = math.atan2(self._x2,self._y2)
        self._off_fr = np.array([self._t1, math.pi/2-self._t1, math.pi/2])
        self._off_fl = np.array([math.pi-self._t1, self._t1-math.pi/2, -math.pi/2])
        self._off_bl = np.array([self._t2-math.pi, -math.pi/2-self._t2, -math.pi/2])
        self._off_br = np.array([-self._t2, self._t2+math.pi/2, -math.pi/2])

    def offset(self, legIndex):
        match legIndex:
            case 0:
                return self._off_fr
            case 1:
                return self._off_fl
            case 2:
                return self._off_bl
            case 3:
                return self._off_br
    
    def link(self, legIndex):
        match legIndex:
            case 0:
                return self._fr
            case 1:
                return self._fl
            case 2:
                return self._bl
            case 3:
                return self._br
            
        



   



