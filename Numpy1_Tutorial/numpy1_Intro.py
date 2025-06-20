#Numpy is a Python library used for working with arrays.
#Numpy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
#Numpy stands for Numerical Python.

import numpy as np
arr=np.array([1,2,3,4,5])
print("Array -",arr)

print("Numpy version -",np.__version__)

print("Type -",type(arr))

#0-D array
arr1=np.array(32)
print("0D-Array -",arr1)

#1-D array
arr2=np.array([2,3,4,6,6])
print("1D-Array -",arr2)

#2-D array
arr3=np.array([[1,2,3,4],[3,4,5,6]])
print("2D-Array -",arr3)

#3-D array
arr4=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3D-Array -",arr4)

a=np.array(42)
b=np.array([1,2,3,4])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,4,5]],[[3,4,5],[9,8,7]]])
print("Dimension -",a.ndim)
print("Dimension -",b.ndim)
print("Dimension -",c.ndim)
print("Dimension -",d.ndim)

#higher dimensional array
#ndmin
arr4=np.array([67,87,98,72,76],ndmin=3)
print("Number of dimensions -",arr4.ndim)






