#Numpy array splitting
#splitting means breaking one array into multiple arrays

import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,2)
print(newarr)

newarr1=np.array_split(arr,3)
print(newarr1)

arr1=np.array([1,2,3,4,5,6])
newarr2=np.array_split(arr,3)
print(newarr2[0])
print(newarr2[1])
print(newarr2[2])

arr2=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr3=np.array_split(arr2,1)
print(newarr3)

