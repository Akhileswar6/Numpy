#Numpy logs

import numpy as np
arr=np.arange(1,10)
print(np.log2(arr))

arr2=np.arange(1,10)
print(np.log10(arr2))

#log-> natural logarithm
arr3=np.arange(1,10)
print(np.log(arr3))

#log at any base
from math import log
arr4=np.frompyfunc(log, 2,1)
print(arr4(100,15))