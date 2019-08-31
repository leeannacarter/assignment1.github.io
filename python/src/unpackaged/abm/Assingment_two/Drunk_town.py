# Imported modules from pythons library.
import csv
import matplotlib.pyplot
import numpy

# Made 25 drunk agents.
# Made 25 homes belonging to each drunk.
# Created a empty list to append the house values to.
# created a empty town list to convert the csv file to a 2d list to plot on a grid.
drunk_agents = 25
num_of_houses = 25
house_num = []
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
    house_num.append(interval * counter)
    counter +=1  # Iterates the loop by 1 until it reaches 25.
#print(house_num)  test

#loops through the row of the town file, the the values in the row to find coordinates /n
#relating to the binary 1's and append to the pub list.
for y, row in enumerate(town):
    for x, value in enumerate(row):
        if value == 1:
            pub.append([y, x])
print(pub)  

#loops through each proeprty number and appends the coordinates that matches each number /n
# which is the house and adds the values to a new houses list.
for prop in house_num:
    for y, row in enumerate(town):
        for x, value in enumerate(row):
            if value == prop:
                houses.append([value, y, x]) # house number, y and x coordinates
print(houses) 
#plots the values to show the towns' environment as file is a raster image.
#plots the location of the pub.
#shows the raster image which inlcudes the houses.  
matplotlib.pyplot.imshow(town)
matplotlib.pyplot.scatter(pub[0][0], pub[0][1])
matplotlib.pyplot.show() 