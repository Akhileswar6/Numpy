#array creation from another python structures
import numpy as np  
listarray=np.array([9,8,6,4,5,1])
print(listarray)
print(listarray.dtype)
print(listarray.size)
print(listarray.shape)

#zeros
zeros=np.zeros((2,5))
print(zeros)

#arange
range_array=np.arange(15)
print(range_array)

#linspace
line_space=np.linspace(1,5,10)
print(line_space)

#empty
emp=np.empty((4,6))
print(emp)

#identity matrix
ide=np.identity(45)
print(ide)

#reshaping & ravel
arr1=np.arange(99)
print(arr1) 
print(arr1.reshape(3,33))
print(arr1.ravel())

x=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(x)
print(arr.sum(axis=0))
print(arr.sum(axis=1))

#transpose
print(arr.T)

#flatten
for i in arr.flat:
    print(i)
print(arr.flatten())

#ndim
print(arr.ndim)

#itemsize
print(arr.nbytes)

#argmax & argmin
print("maximum value index",arr.argmax())
print("minimum value index",arr.argmin())

print("maximum value index",arr.argmax(axis=0))
print("minimum value index",arr.argmin(axis=1))

#argsort
print(arr.argsort())
  
#find
print(np.where(arr>5))

print(np.count_nonzero(arr))

import sys
ch_ar=[0,4,55,2]
np_ar=np.array(ch_ar)
print(sys.getsizeof(1)*len(ch_ar))



