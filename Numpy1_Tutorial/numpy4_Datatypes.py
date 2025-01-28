#Numpy Datatypes

#i-> integer
#b-> boolean
#u-> unsigned integer
#f-> float
#c-> complex float
#m-> timedelta
#M-> datetime
#O-> object
#S-> string
#U-> unicode string
#V-> fixed chunk of memory for other type (void)

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.dtype)

arr1=np.array(["apple","banana","cherry"])
print(arr1.dtype)

#Creating array with defined data type
arr2=np.array([2,3,4,5], dtype='S')
print(arr2.dtype)

arr3=np.array([1,2,3,4], dtype="i4")
print(arr3.dtype)

#value error
# arr4=np.array(["a","2","3","4"], dtype="i")
# print(arr4.dtype)

#converting data type on existing arrays
#astype()-> makes a copy of the array and allows you to specify the data type as a parameter
arr5=np.array([1.34,2.46,4.98,9.45])
newarr=arr5.astype(int)
print(newarr)
print(newarr.dtype)

arr6=np.array([1,2,3,4,5,78])
newarr1=arr6.astype("f")
print(newarr1)

arr7=np.array([-1,0,3,98,0,5])
newarr2=arr7.astype(bool)
print(newarr2)

