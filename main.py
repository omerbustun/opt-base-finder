#!/usr/bin/env python
import numpy as np

H = int(input("Enter height: "))
W = int(input("Enter width: "))
U = int(input("Enter number of users: "))

area = np.zeros((H ,W)) #creates a 10 by 10 area matrix and populates it with zeros

area.flat[np.random.choice(H * W, U, replace=False)] = 1 #flattens the matrix to an array, randomly selects 10 values and changes them to 1
print(area)

ones = np.where(area == 1)
listOfIndices = list(zip(ones[0], ones[1]))
distances = []
energyCostMid = []
energyCostOpt = []
energyCostOptLocal = []
class costData:
   def __init__(self, x, y, cost):
      self.x = x
      self.y = y
      self.cost = cost

for indice in listOfIndices:
   distances.append(np.sqrt(((abs(H//2 - indice[0]))**2) + ((abs(W//2 - indice[1]))**2)))

for distance in distances:
   energyCostMid.append(distance**2)

for i in range(H):
   for j in range(W):
      energyCostOptLocal.clear()
      for indice in listOfIndices:
         energyCostOptLocal.append(np.sqrt(((abs(i - indice[0]))**2) + ((abs(j - indice[1]))**2)))
      energyCostOpt.append(costData(i, j, sum(energyCostOptLocal)))

energyCostOpt.sort(key=lambda x: x.cost)

print(f"Total energy consumption when the base tower is in the middle: {sum(energyCostMid)}")
print(f"Optimum coordinates for optimum energy consumption: X: {energyCostOpt[0].x} Y: {energyCostOpt[0].y}")
print(f"Total energy consumption when the base tower is in the optimum coordinates: {energyCostOpt[0].cost}")