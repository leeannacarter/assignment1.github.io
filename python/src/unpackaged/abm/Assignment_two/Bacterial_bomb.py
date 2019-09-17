# Imported modules from pythons library.
import csv
import spread
import matplotlib
import matplotlib.pyplot


# Created an empty list to append the bomb environment to.
# Created an empty list to append the bomb location to.
# Created 5000 agents.
# created an empty bacteria agents list. 
num_of_agents = 5000
bacteria = []
environment = []
bomb = []

# Opens and read in the csv datafile of the bomb environment.
# Parses the file to a 2d list.
file = open("wind.raster.txt")
dataset = csv.reader(file, delimiter=",")
# for line in dataset:
#    print(line) # loops through the file to print each row (test).
for row in dataset:
    rowlist = []
    for values in row:
        rowlist.append(int(values))
    environment.append(rowlist)
#print(environment)    #test
file.close()

# loops through the row of the environment file, then the values in the row to find coordinates /n
# relating to the binary 255's (bomb point) to append it to the bomb list.
for y, row in enumerate(environment):
    for x, value in enumerate(row):
        if value == 255:
            bomb.append([y, x])
#print(bomb)  #test

# Plots a size 7x7 figure.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents through adding the random functions to  an empty list.
# the spread class method is appened to the agent list.
# the environment, bacteria agents and bomb is appended to the spread class to allow access to one another.
for i in range(num_of_agents):
    bacteria.append(spread.Agent(environment, bacteria, bomb))

#a = spread.Agent(environment, bacteria, bomb)
#print(a.y, a.x) # test the return of get y and x.

# iterates through 5000 bacteria.
# while loop takes each agent and connects them to the spread and height class calculations to move.
#The answers are plotted to a graph.
for i in range(num_of_agents):
    while bacteria[i].z > 0:
        bacteria[i].move()
        bacteria[i].height()
#       print(bacteria[i].y, bacteria[i].x) # test to see if the bacteria calculations have worked.
    environment[bacteria[i].y][bacteria[i].x] += 1 

# plots the y and x location of the bomb.
# plots the raster x and y values 300x300 on  grid.
#plots the density of the bacterial agents using a copper colour ramp.
matplotlib.pyplot.scatter(bomb[0][0], bomb[0][1])
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.imshow(environment, cmap='copper') 
matplotlib.pyplot.show() 