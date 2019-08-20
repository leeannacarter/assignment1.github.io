# Imported modules from pythons library.
import csv
import matplotlib.pyplot

# Made 25 drunk agents.
# Made 25 homes belonging to each drunk.
# Created a empty list to append the house values to.
# created a empty town list to convert the csv file to a 2d list to plot on a grid.
drunk_agents = 25
num_of_houses = 25
houses = []
town = []
counter = 1    # used a counter to map 25 houses.

# Opens and read in the csv datafile of the town environment.
# Parses the file to a 2d list.
file = open("drunk.plan.txt")
dataset = csv.reader(file, delimiter=",")
#for line in dataset:
#    print(line) # loops through the file to print each row (test).
for row in dataset:
    rowlist = []
    for values in row:
        rowlist.append(int(values))
    town.append(rowlist)
print(town)    
file.close()


# while count reaches to 25, vales from (10x25) will be added to the empty houses list
while counter <= num_of_houses:
    interval = 10
    houses.append(interval * counter)
    counter +=1
print(houses)


#plots and show the town's 2d list environment as list is a raster file.  
matplotlib.pyplot.imshow(town)
matplotlib.pyplot.show() 