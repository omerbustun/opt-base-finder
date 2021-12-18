#!/usr/bin/env python
import numpy as np

H = int(input("Enter height: "))
W = int(input("Enter width: "))
S = int(input("Enter number of subscribers: "))

area = np.zeros((H ,W)) #creates a 10 by 10 area matrix and populates it with zeros

area.flat[np.random.choice(H * W, S, replace=False)] = 1 #flattens the matrix to an array, randomly selects 10 values and changes them to 1
print(area)

subs = np.where(area == 1)
listOfIndices = list(zip(subs[0], subs[1]))
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

print(f"Energy con. with BS in the center: {round(sum(energyCostMid), 2)}")
print(f"Optimum coordinates: X: {energyCostOpt[0].y + 1} Y: {energyCostOpt[0].x + 1}")
print(f"Energy con. with BS in the opt. coordinates: {round(energyCostOpt[0].cost, 2)}")