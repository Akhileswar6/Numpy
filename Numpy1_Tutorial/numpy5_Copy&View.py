#Numpy array copy and view
#copy-> copy the original array and its data, changes doesn't affect original array
#view-> view of the original array, changes affects the original array

#copy
import numpy as np
arr=np.array([2,3,323,12,56])
x=arr.copy()
arr[2]=67
print("Modified Array -",arr)
print("Copy Array -",x)

#view
arr1=np.array([34,56,6789,4575,56])
y=arr1.view()
arr1[2]=34
print(y)

#check if array owns its data
#base-> property returns None if array owns the data
arr2=np.array([1,2,3,4,5])
x1=arr2.copy()
x2=arr2.view()
print(x1.base)
print(x2.base)


