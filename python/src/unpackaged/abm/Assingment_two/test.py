import csv
import matplotlib.pyplot

town = []

pub = []

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

for y, row in enumerate(town):
    for x, value in enumerate(row):
        if value == 1:
            pub.append([y, x])
print(pub)        
   
#matplotlib.pyplot.imshow(town)
#matplotlib.pyplot.show()

