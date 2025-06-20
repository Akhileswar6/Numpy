#Numpy array join
#joining means putting contents of two oor more arrays in a single array.

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print("Concatenate -",arr)

arr3=np.array([[1,2],[3,4]])
arr4=np.array([[5,6],[7,8]])
arr5=np.concatenate((arr3,arr4), axis=1)
print("Concatenate -",arr5)

#joining arrays using stack function
arr6=np.array([1,2,3])
arr7=np.array([4,5,6])
arr8=np.stack((arr6,arr7), axis=1)
print("Concatenate -",arr8)

#stacking along rows
arr9 = np.array([1, 2, 3])
arr10 = np.array([4, 5, 6])
arr11= np.hstack((arr9, arr10))
print(arr11)

#stacking along columns
arr12=np.array([1,23,6])
arr13=np.array([34,89,65])
arr14=np.vstack((arr12, arr13))
print(arr14)
