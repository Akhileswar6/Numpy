#Numpy array searching
#searching-> searching an array for a certain value

import numpy as np
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)

arr1=np.array([1,2,3,4,5,6,7,8])
x1=np.where(arr1%2==0)
print(x1)
x2=np.where(arr1%2!=0)
print(x2)

#search sorted-> it is used on sorted arrays
arr2=np.array([5,34,56,78,89])
x3=np.searchsorted(arr2,56)
print(x3)

#search from the right side
arr5=np.array([6,7,8,9])
x4=np.searchsorted(arr5,9, side='right')
print(x4)

#finding multiple values
arr6=np.array([1,3,5,7])
x5=np.searchsorted(arr6,[2,4,6])
print(x5)
