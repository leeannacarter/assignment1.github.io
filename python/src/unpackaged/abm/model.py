# Imported modules from pythons' library.
import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import time
import agentframework
import csv
import random

# Times how long the code starts to run.
start = time.process_time()

# Created 10 agents.
# Created 100 iterations to move the agents that many times.
# Created an empty list to add the x and y values to (agents).
# Created an empty environment lists to add the in.txt data into.
# Created a neighbourhood variable to allow agents to communicate with each other.    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
environment = []

# Open and reads through a csv formatted file saved within my directory.
# Loops through the rows and columns of the csv file, adding the rows to the empty rowlist.
# Values within rowlist is then added to the empty environment list.
file = open("in.txt")
dataset = csv.reader(file, delimiter=",")
for row in dataset:
    rowlist = []
    for values in row:
        #print(values) to a 2d list to read with the environment grid.
        rowlist.append(int(values))
    environment.append(rowlist)
print(environment)
file.close()

# Creates an animated figure.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)


# Make the agents through adding the random functions to  an empty list.
# Append the environment values for each agent to share.
# Agents can access each other through adding the agents list within Agents class.
for i in range(num_of_agents):
     agents.append(agentframework.Agent(environment, agents))

# Assigned a true boolean to support a stopping condition.
carry_on = True    

# Builds an animation of the agent base model.
# Use's the global carry_on variable within its local environment.
def update(frame_number):
    fig.clear()
    global carry_on
    
# Move the agents.
# Eats the agents.
# Agents shares resources with one another if within 20 units from each other.   
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            #randomly shuffles the order of agents more.
            random.shuffle([i])
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)  
#           tests to see if the agents list is accessible
#           print(agents[i].environment, agents[i].store)
            
# Test to see if y and x generates a random number from the Agent class.
# a = agentframework.Agent()
# print(a.y, a.x)

# Stops the agents from moving if random number is less than 0.1.
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

# The animation will run until 'a' appraoches 9 (increments in 1's) as long as it equals true.   
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on):
        yield a			# Returns control and waits next call.
        a += 1
# Repeatedly calls functions to process an animation for the agent model. It also runs in an infinite loop using binary false.
# Animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

# sets the y and x limited within a grid.
# Imshow plots the raster image (environment).
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() 

#times how long the code takes to end.
end = time.process_time()
print("time = " + str(end - start))



#loops through the agents which has been appended to an empty agents list.
#Calculates the distance between y and x values within the for loop.
#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b) 
#        print(distance)
 

