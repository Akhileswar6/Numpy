#Slicing Arrays

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print("Slicing of [1:5] -",arr[1:5])
print("Slicing of [4:] -",arr[4:])
print("Slicing of [:4] -",arr[:4])
print("Slicing of [-6:] -",arr[-6:])
print("Slicing of [-5:-1] -",arr[-5:-1])
print("Slicing of [0:5:2] -",arr[0:5:2])
print("Slicing of [::2] -",arr[::2])
print("Slicing of [::3] -",arr[::3])

#Slicing 2-D arrays
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])  

print("Slicing of [0,2:] -",arr1[0,2:])
print("Slicing of [1,:] -",arr1[1,:])
print("Slicing of [1,0:4:2] -",arr1[1,0:4:2])

#from both elements, return index 2
print("from both elements, return index 2 -",arr1[0:2,2])

#from both elements, return index 3
print("from both elements, return index 3 -",arr1[0:2,3])

#from both elements, slice index 1 to index 4
print("from both elements, slice index 1 to index 4 -",arr1[0:2,1:4])

#from the both elements , slice index 0 to last index with step value 2
print("from the both elements , slice index 0 to last index with step value 2 -",arr1[0:2,0:5:2])