#Numpy differences

import numpy as np
arr=np.array([10,12,23,5])
newarr=np.diff(arr)
print(newarr)

arr1=np.array([10,15,25,5])
newarr=np.diff(arr1,n=2)
print(newarr)

