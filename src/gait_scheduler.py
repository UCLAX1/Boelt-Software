#The gait scheduler is responsible for planning which feet should be on the ground (stance) 
#and which should be moving forward to the next step (swing) at any given time. 

class GaitScheduler:
    def __init__(self, config):
        self.config = config
    
    def whichFeetOnGround(self, state):
        if(state == 0 or state == -1): #Rest or Deactivated
            self.currentStance = np.array([1,1,1,1])
        elif(state == 1): #Walk -> pi/2 between each state
            if(self.currentStance == self.contact_phases[0]): 
                self.currentStance = self.contact_phases[1]
            elif(self.currentStance == self.contact_phases[1]):
                self.currentStance = self.contact_phases[2]
            elif(self.currentStance == self.contact_phases[2]):
                self.currentStance = self.contact_phases[3]
            if(self.currentStance == self.contact_phases[3]): 
                self.currentStance = self.contact_phases[4]
            elif(self.currentStance == self.contact_phases[4]):
                self.currentStance = self.contact_phases[5]
            elif(self.currentStance == self.contact_phases[5]):
                self.currentStance = self.contact_phases[6]
            if(self.currentStance == self.contact_phases[6]): 
                self.currentStance = self.contact_phases[7]
            else:
                self.currentStance = self.contact_phases[0]
