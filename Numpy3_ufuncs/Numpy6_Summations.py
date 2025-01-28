#Numpy summations
#summation-> adds all elements in an array

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
newarr1=np.sum([arr1,arr2])
print(newarr1)

#summation over an axis
#numpy will sum the numbers in each array.
arr3=np.array([78,98,76])
arr4=np.array([23,45,67])
newarrr2=np.sum([arr3,arr4],axis=1)
print(newarrr2)


#Cummulative sum
#The cummalatve sum means partially adding the elements in array.
#E.g. The partial sum of [1,2,3,4] will be [1,1+2,1+2+3,1+2+3+4]=[1,3,6,10]
arr5=np.array([12,23,3,24])
newarr3=np.cumsum(arr5)
print(newarr3)

