#Rounding decimals

#truncation-> remove the decimals and return the float number closest to zero.
#use trunc() or fix() function

import numpy as np
arr=np.trunc([-3.1666, 3.6667])
print(arr)

#Rounding
#around-> function increments preceding digit or decimal by 1 if >=5 else do nothing.
arr1=np.around(3.1666,2)
print(arr1)

#floor-> rounds off decimal to nearest lower integer.
arr2=np.floor([-3.1666, 3.6667])
print(arr2)

#ceil-> function rounds off decimal to nearest upper integer
arr3=np.ceil([-3.1666, 3.6667])
print(arr3)

