#!/usr/bin/env python
import numpy as np

area = np.zeros((10,10)) #creating a 10 by 10 area matrix and populating it with zeros

area.flat[np.random.choice(10 * 10, 10, replace=False)] = 1 #flattens the matrix to an array, randomly selects 10 values and changes them to 1

print(area)