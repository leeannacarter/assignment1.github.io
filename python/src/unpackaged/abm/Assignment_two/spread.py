#imported modules from the python library.
import random

class Agent:
    def __init__(self, environment, bacteria, bomb):
        self.environment = environment
        self.agent = bacteria
        self.y = bomb[0][1]
        self.x = bomb[0][0]
        self.z = 75

# Returns the outcome of the x and y variables.   
    def get_yx(self):
        return self.y, self.x
    
# Moves the y and x agents at a 2d perspective.
    def move(self):
        wind = random.random()
        
        if wind <= 0.75:
            self.x = (self.x + 1) % 300 # move East by 75%

        elif wind > 0.75 and wind <= 0.85:
            self.y = (self.y + 1) % 300 # move North or South by 10%
        
        elif wind > 0.85 and wind <= 0.95:
            self.y = (self.y - 1) % 300 # move West by 5%
        
        else:
            self.x = (self.x - 1) % 300  # move West by 5%

# moves the y and x agents up and down at a 3d persective.
    def height(self):
        
        if self.z < 75: # bacteria will not fall
            self.z = (self.z - 1) 
        else:
            turbulance = random.random()

            if turbulance <= 0.7: # 70% the bacteria will fall
                self.z = (self.z - 1) 
            
            elif turbulance > 0.7 and turbulance <= 0.9: #20% the bacteria will rise.
                self.z = (self.z + 1) 
                
            else:
                self.z = self.z  # the bacteria will stay at the same level.
    