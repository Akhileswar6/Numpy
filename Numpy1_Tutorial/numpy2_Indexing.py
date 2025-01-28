#Numpy Array indexing

import numpy as np
arr=np.array([34,45,56,67])
print(arr[0])
print(arr[1])
print(arr[2])

print(arr[2]+arr[3])
print(arr+arr[0])

#Access 2-D array
arr1=np.array([[34,45,12,13,78],[23,34,12,78,26]])
print("3rd element on 2nd dim:",arr1[1,2])
print("5th element on 2nd dim:",arr1[1,4])

#Access 3-D array
arr2=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,42,1]],[[1,2,3],[3,45,6]]])
print(arr2[1,1,1])
print(arr2[1,0,2])
print(arr2[2,1,2])

#Negative indexing
arr3=np.array([[11,12,13,14,15],[21,22,23,24,25]])
print(arr3[1,-3])
print(arr3[0,-5])

