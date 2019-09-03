# Imported modules from pythons library.
import csv
import matplotlib.pyplot
import journey
import statistics

# Created 25 drunk agents.
# Created 25 homes belonging to each drunk.
# Created an empty drunk agents list to store the y and x moving locations.
# Created an empty list to append the house values to (door numbers).
# Created an empty list to append the houses coordinates within.
# Created an empty town list to convert the csv file to a 2d list to plot on a grid.
# Created an empty list to append the pub coordinate within.
num_of_agents = 25
num_of_houses = 25
drunk_agents = []
door_num = []
houses = []
town = []
pub = []
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
#print(town)    test
file.close()


# while count reaches to 25, values from (10x25) are added to the empty houses list.
# list or door numbers.
while counter <= num_of_houses:
    interval = 10
    door_num.append(interval * counter)
    counter +=1  # Iterates the loop by 1 until it reaches 25.
#print(house_num)  test

#loops through the row of the town file, then the values in the row to find coordinates /n
#relating to the binary 1's and append to the pub list.
for y, row in enumerate(town):
    for x, value in enumerate(row):
        if value == 1:
            pub.append([y, x])
print(pub)  

#loops through each proeprty number, row in town and value in row to appends the coordinates that matches each door number /n
# which is the house and adds the values to a new houses list.
for prop in door_num:
    for y, row in enumerate(town):
        for x, value in enumerate(row):
            if value == prop:
                houses.append([value, y, x]) # house number, y and x coordinates
print(houses) 

#loops through 25 agents and appends it to n empty drunk agents list.
# the journey class method is appened to the agent list.
# the town environment, drunk agetns and pub is appended to the journery class to allow access to one another.
for i in range(num_of_agents):
    drunk_agents.append(journey.Walk(town, drunk_agents, pub, num_of_houses))
    
    
#plots the values to show the towns' environment as file is a raster image.
#plots the location of the pub.
#shows the raster image which inlcudes the houses.  
matplotlib.pyplot.imshow(town)
matplotlib.pyplot.scatter(pub[0][0], pub[0][1])
matplotlib.pyplot.show() 