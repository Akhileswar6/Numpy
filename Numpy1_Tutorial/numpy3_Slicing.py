#Slicing Arrays

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-6:])
print(arr[-5:-1])
print(arr[0:5:2])
print(arr[::2])
print(arr[::3])

#Slicing 2-D arrays
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])  

print(arr1[0,2:])
print(arr1[1,:])
print(arr1[1,0:4:2])

#from both elements, return index 2
print(arr1[0:2,2])

#from both elements, return index 3
print(arr1[0:2,3])

#from both elements, slice index 1 to index 4
print(arr1[0:2,1:4])

#from the both elements , slice index 0 to last index with step value 2
print(arr1[0:2,0:5:2])