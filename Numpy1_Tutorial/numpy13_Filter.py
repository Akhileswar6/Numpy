#Numpy array filter
#getting some elements out of an existing array and creating a new array out of them is called filtering

import numpy as np
arr=np.array([41,42,43,45])
x=[True,False,True,False]
newarr=arr[x]
print(newarr)

arr1=np.array([41,42,43,44])    
filter_arr=[]
for element in arr1:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr1=arr1[filter_arr]
print(filter_arr)
print(newarr1)

arr2=np.array([23,87,99,67,45,32,34,78])
filter_arr1=[]
for i in arr2:
    if i %2==0:
        filter_arr1.append(True)
    else:
        filter_arr1.append(False)
newarr2=arr2[filter_arr1]
print(filter_arr1)
print(newarr2)

arr3=np.array([32,76,42,14,23])
filter_arr3=arr3>40
newarr3=arr3[filter_arr3]
print(filter_arr3)
print(newarr3)
