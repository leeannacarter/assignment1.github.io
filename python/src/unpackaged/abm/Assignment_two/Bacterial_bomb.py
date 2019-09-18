# Imported modules from pythons library.
import csv
import spread
import matplotlib
import matplotlib.pyplot

# Created 5000 agents.
# created an empty bacteria agents list. 
# Created an empty list to append the bomb environment to.
# Created an empty list to append the bomb location to.
num_of_agents = 5000
bacteria = []
environment = []
bomb = []

# Opens and read in the csv datafile of the bomb environment.
# Parses the file to a 2d list.
file = open("wind.raster.txt")
dataset = csv.reader(file, delimiter=",")
# for line in dataset:
#    print(line) # test: iterates through the file to print each row.
for row in dataset:
    rowlist = []
    for values in row:
        rowlist.append(int(values))
    environment.append(rowlist)
#print(environment)    #test: iterates through to create a 2d list.
file.close()

# loops through the rows of the environment file, then the values in the rows to find coordinates /n
# relating to the binary 255's (bomb point) to append it to the bomb list.
for y, row in enumerate(environment):
    for x, value in enumerate(row):
        if value == 255:
            bomb.append([y, x])
#print(bomb)  #test: prints the location of the bomb.

# Plots a size 7x7 figure.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents through adding the random functions to  an empty list.
# the spread class method is appended to the agent list.
# the environment, bacterial agents and bomb is appended to the spread class to allow access to one another.
for i in range(num_of_agents):
    bacteria.append(spread.Agent(environment, bacteria, bomb))

#a = spread.Agent(environment, bacteria, bomb)
#print(a.y, a.x) # test: return the y and x variables.

# iterates through 5000 bacteria.
# while loop takes each agent and connects them to the spread and height class methods to move.
#The density formed from the spread class methods are plotted to a graph.
# plots the density.
for i in range(num_of_agents):
    while bacteria[i].z > 0:
        bacteria[i].move()
        bacteria[i].height()
#       print(bacteria[i].y, bacteria[i].x) # test: the Spread class has generated answers.
    environment[bacteria[i].y][bacteria[i].x] += 1 
matplotlib.pyplot.imshow(environment, cmap='copper') 

# plots the y and x location of the bomb.
# plots the raster x and y values 300x300 on  grid.
# plots the density of the bacterial agents using a copper colour ramp.
# shows the density pattern as an image.
matplotlib.pyplot.scatter(bacteria[i].y, bacteria[i].x)
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.show() 

#saved the density graph to a file as text.
with open('density_graph.txt', 'w') as graph:
    graph.write("matplotlib.pyplot.imshow(environment, cmap='copper'")
graph.close()