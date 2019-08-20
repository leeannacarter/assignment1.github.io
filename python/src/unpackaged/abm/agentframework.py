# Imported random module to assist in generating random numbers for x and y locations.
import random

# Created class agent, setting x and y variables to the random function.
# Appended the environment values within this class to share from my main model.
# Appended the agents list values within this class to link with the agents.
# Store saves the eaten environment for each agent.
class Agent:
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.neighbourhood = 20
                
# Returns the outcome of the x and y variables.   
    def get_xy(self):
        return self.x, self.y
                 
# Moves the agents twice.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

# Eats 10 values within the environment if the random number generated is above 10.
# 10 is taken away and stored within store.          
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
  
# Identifies if each agents are within 20 unit from each other. If so, their current variables
# Will changes to share space with one another at an average distance (object-object communication).
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                print("sharing " + str(dist) + " " + str(ave))

# Created a function to calculate the distance between coordinates (agents).                
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 