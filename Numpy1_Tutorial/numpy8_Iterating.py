#Numpy array iterating

import numpy as np
arr=np.array([1,2,3,4,5,98])
for i in arr:
    print(i)

#iterating 2-D arrays
arr1=np.array([[1,2,3,4],[5,6,7,8]])
for j in arr1:
    print(j)
    for x in j:
        print(x)

#iterating 3-D arrays
arr2=np.array([[[1,23,12],[24,12,67]],[[12,89,9],[98,987,6]]])
for k in arr2:
    for y in k:
        for z in y:
            print(z)

#iterating using nditer()
arr3=np.array([[[12,13],[14,15]],[[16,17],[18,19]]])
for a in np.nditer(arr3):
    print(a)

#iterating array with different data types
arr4=np.array([1,2,3])
for s in np.nditer(arr4, flags=["buffered"], op_dtypes=["float"]):
    print(s)

#enumerated iteration using ndenumerate()
arr5=np.array([1,2,545,2,5])
for idx, v in np.ndenumerate(arr5):
    print(idx, v)

arr6=np.array([[1,2,3,4],[5,6,7,8]])
for idx, sa in np.ndenumerate(arr6):
    for idx1, sa1 in np.ndenumerate(sa):
        print(idx, idx1, sa1)