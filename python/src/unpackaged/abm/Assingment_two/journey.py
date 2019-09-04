#imported moduels from the python library.
import random

# created agents y and x locations to randomly select a pair of coordinates from the pub list.
# appended the agents town environment.
# appended the agents to enabe interaction with one another.
# appended the pub to allow agents to access.
# created store to store the density of each agents walk.
class Agent:
    def __init__(self, town, drunk_agents, pub):
        self.y = random.choice(range(pub[0][0]))
        self.x = random.choice(range(pub[0][1]))
        self.town = town
        self.agents = drunk_agents
        self.pub = pub
        self.store = 0

# Returns the outcome of the x and y variables.   
    def get_yx(self):
        return self.y, self.x
    
# Moves the y and x agents twice.
    def walk(self):
        
        if random.random() < 0.5:
            self.y += 1 % 300
        else:
            self.y += 1 % 300

        if random.random() < 0.5:
            self.x += 1 % 300
        else:
            self.x += 1 % 300
        
#    def density(self):
#        if self.environment[self.y][self.x] > 10:
#            self.environment[self.y][self.x] -= 10
#            self.store += 10
            
            
            
            
            
            
