#imported moduels from the python library.
import random

class Agent:
    def __init__(self, environment, bomb, bacteria):
        self.y = bomb[0][0]
        self.x = bomb[0][1]
        self.environment = environment
        self.bacteria = bacteria
        self.store = 0

# Returns the outcome of the x and y variables.   
    def get_yx(self):
        return self.y, self.x
    
# Moves the y and x agents twice.
    def spread(self):
        move = random.random
        
        if move <= 0.05:
            self.x = (self.x - 1) % 300 # move West

        elif move > 0.05 and <= 0.15:
            self.y = (self.y + 1) % 300 # move North or South
        
        elif move > 0.15 and <= 0.25:
            self.y = (self.y - 1) % 300 # move East
        
        else 
            self.x = (self.x + 1) % 300  
