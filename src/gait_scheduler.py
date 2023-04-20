#The gait scheduler is responsible for planning which feet should be on the ground (stance) 
#and which should be moving forward to the next step (swing) at any given time. 
#In a trot for example, the diagonal pairs of legs move in sync and take turns between stance and swing

class GaitScheduler:
    def __init__(self, config):
        self.config = config
    
    def whichFeetOnGround(self, state):
        if(state == 0 or state == -1):
            self.nextStance = [1,1,1,1]
        elif(state == 1):
            if(self.prevStance == [0,1,0,1]):
                self.nextStance = [1,0,1,0]
            else:
                self.nextStance = [0,1,0,1]
