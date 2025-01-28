#Numpy products
#Product-> multiplies all elements in an array
import numpy as np
arr=np.array([1,2,3,4])
x=np.prod(arr)
print(x)

#find the product of two arrays
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
newarr=np.prod([arr1,arr2])
print(newarr)

#product over an axis
arr3=np.array([1,2,3,4])
arr4=np.array([5,6,7,8])
newarr1=np.prod([arr3,arr4], axis=1)
print(newarr1)

#Cummulative product
arr5=np.array([1,2,3,4])
newarr2=np.cumprod(arr5)
print(newarr2)