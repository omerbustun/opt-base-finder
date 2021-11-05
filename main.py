#!/usr/bin/env python
import numpy as np

H = 10 #int(input("Enter height: "))
W = 10 #int(input("Enter width: "))
U = 10 #int(input("Enter number of users: "))

area = np.zeros((H ,W)) #creates a 10 by 10 area matrix and populates it with zeros

area.flat[np.random.choice(H * W, U, replace=False)] = 1 #flattens the matrix to an array, randomly selects 10 values and changes them to 1
print(area)

ones = np.where(area ==1)
listOfIndices = list(zip(ones[0], ones[1]))
distances = []
energyCost = []

for indice in listOfIndices:
   distances.append(np.sqrt(((abs(5 - indice[0]))**2) + ((abs(5 - indice[1]))**2)))

for distance in distances:
   energyCost.append(distance**2)

print("Total energy consumption when the base tower is in the middle: ", sum(energyCost))