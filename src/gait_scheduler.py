#The gait scheduler is responsible for planning which feet should be on the ground (stance) 
#and which should be moving forward to the next step (swing) at any given time. 

class GaitScheduler:
    def __init__(self, config):
        self.config = config
    
    def whichFeetOnGround(self, state):
        if(state == 0 or state == -1): #Rest or Deactivated
            self.nextStance = np.array([1,1,1,1])
            self.prevStance = np.array([1,1,1,1])
        elif(state == 1): #Walk -> pi/2 between each state
            if(self.prevStance == np.array([1,0,1,1])): 
                self.nextStance = np.array([1,1,1,0])
                self.prevStance = np.array([1,1,1,0])
            elif(self.prevStance == np.array([1,1,1,0])):
                self.nextStance = np.array([0,1,1,1])
                self.prevStance = np.array([0,1,1,1])
            elif(self.prevStance == np.array([0,1,1,1])):
                self.nextStance = np.array([1,1,0,1])
                self.prevStance = np.array([1,1,0,1])
            else:
                self.nextStance = np.array([1,0,1,1])
                self.prevStance = np.array([1,0,1,1])
