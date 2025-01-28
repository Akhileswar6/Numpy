#Numpy array reshaping
#reshape-> means changing the shape of an array

#reshape from 1-D to 2-D
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(6,2)
print(newarr)

#reshape from 1-D to 3-D
arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr1=arr1.reshape(2,3,2)
print(newarr1)

arr2=np.array([1,2,3,4,5,6,7,8])
print(arr2.reshape(2,4).base)

arr3=np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr2=arr.reshape(3,2,-1)
print(newarr2)

#flattening the arrays
#flattening-> converting a multidimensional array into a 1-D array
arr4=np.array([[12,12,23],[23,45,67]])
newarr3=arr4.reshape(-1)
print(newarr3)


