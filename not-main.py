#!/usr/bin/env python
import numpy as np

H = 10 #height of the area matrix
W = 10 #width of the area matrix
U = 10 #number of users in the area


area = np.zeros((H ,W)) #creates a 10 by 10 area matrix and populates it with zeros
print(area)

def sel_x_value(H , W, U):
   area.flat[np.random.choice(H * W, U, replace=False)] = 1 #flattens the matrix to an      array, randomly selects 10 values and changes them to 1
   print(area)

if __name__ == "__main__":
  sel_x_value(H, W, U)
