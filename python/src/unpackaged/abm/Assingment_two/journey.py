#imported moduels from the python library.
import random

#created agents y and x lcoations to equal a random number between.
# appended the agents town environment.
# appended the agents to enabe interaction with one another.
# appended the pub to allow agents to access.
class Walk:
    def __init__(self, town, drunk_agents, pub, num_of_houses):
        self.y = random.randint(0, 300)
        self.x = random.randint(0,300)
        self.environment = town
        self.agents = drunk_agents
        self.pub = pub
        self.store = 0
        self.house = num_of_houses

# Returns the outcome of the x and y variables.   
    def get_xy(self):
        return self.x, self.y
    
# Moves the y and x agents twice.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100