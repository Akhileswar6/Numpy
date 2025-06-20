#Numpy shape manipulation
#shape-> the shape of an array is the number of elements in each dimension

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print("Shape -",arr.shape)

#ndim-> number of dimensions
arr1=np.array([1,2,3,4], ndmin=5)
print(arr1)
print("Shape -",arr1.shape)
