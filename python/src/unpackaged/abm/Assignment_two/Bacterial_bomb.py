# Imported modules from pythons' library.
import csv
import spread
import matplotlib
import matplotlib.pyplot

# Created 5000 agents.
# Created an empty bacteria agents list. 
# Created an empty list to append the bomb environment to.
# Created an empty list to append the bomb location to.
# Created an empty list to append the empty environment binary 'zeros' to (empty spaces).
num_of_agents = 5000
bacteria = []
environment = []
bomb = []
fallout_plot = []

# Opens and read in the csv datafile of the bomb environment.
# Appends the empty spaces to a new list.
# Parses the file to a 2d list.
file = open("wind.raster.txt")
dataset = csv.reader(file, delimiter=",")
# for line in dataset:
#    print(line) # test: iterates through the file to print each row.
for row in dataset:
    fallout_row = []
    rowlist = []
    for values in row:
        rowlist.append(int(values))
        fallout_row.append(0)
    environment.append(rowlist)
    fallout_plot.append(fallout_row)
#print(environment)    #test: iterates through to create a 2d list.
file.close()

# Loops through the rows of the environment file, then the values in the rows to find coordinates /n
# Relating to the binary 255's (bomb point) to append it to the bomb list.
for y, row in enumerate(environment):
    for x, value in enumerate(row):
        if value == 255:
            bomb.append([x, y])
#print(bomb)  #test: prints the location of the bomb.

# Plots a size 7x7 figure.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents through adding the random functions to an empty list.
# The spread class method is appended to the agent list.
# The environment, bacterial agents and bomb is appended to the spread class to allow access to one another.
for i in range(num_of_agents):
    bacteria.append(spread.Agent(environment, bacteria, bomb))

#a = spread.Agent(environment, bacteria, bomb)
#print(a.y, a.x) # test: return the y and x variables.

# Iterates through 5000 bacteria.
# While loop takes each agent and connects them to the spread and height class methods to move.
# The density formed from the spread class methods are plotted to a graph.
# Plots the density.
for i in range(len(bacteria)):
    while bacteria[i].z > 0:
        bacteria[i].move()
        bacteria[i].height()
#        print(bacteria[i].y, bacteria[i].x, bacteria[i].z) # test: Spread and height class function.
    fallout_plot[bacteria[i].y][bacteria[i].x] += 1 
matplotlib.pyplot.imshow(fallout_plot, cmap='YlOrRd') 

# Plots the y and x location of the bomb.
# Plots the raster x and y values 300x300 on  grid.
# Plots the density of the bacterial agents using a yellow-red colour ramp.
# Shows the density pattern as an image.
matplotlib.pyplot.scatter(bomb[0][0], bomb[0][1])
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.show() 

# Save's the density graph to a file as text.
with open('density_graph.txt', 'w') as graph:
    graph.write("matplotlib.pyplot.imshow(environment, cmap='YlOrRd'")
graph.close()