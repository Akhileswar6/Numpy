#Numpy Array indexing

import numpy as np
arr=np.array([34,45,56,67])
print("Index-0 -",arr[0])
print("Index-1 -",arr[1])
print("Index-2 -",arr[2])

print("Addition -",arr[2]+arr[3])
print("Addition1 -",arr+arr[0])

#Access 2-D array
arr1=np.array([[34,45,12,13,78],[23,34,12,78,26]])
print("3rd element on 2nd dim -",arr1[1,2])
print("5th element on 2nd dim -",arr1[1,4])

#Access 3-D array
arr2=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,42,1]],[[1,2,3],[3,45,6]]])
print("Index of [1,1,1] -",arr2[1,1,1])
print("Index of [1,0,2] -",arr2[1,0,2])
print("Index of [2,1,2] -",arr2[2,1,2])

#Negative indexing
arr3=np.array([[11,12,13,14,15],[21,22,23,24,25]])
print("Index of [1,-3] -",arr3[1,-3])
print("Index of [0,-5] -",arr3[0,-5])

