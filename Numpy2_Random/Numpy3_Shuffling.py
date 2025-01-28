#Random permutations
#a permutation refers to sn arrangement of elements. eg: [3,2,1] is a permutation of [1,2,3]

#shuffling arrays
#shuffling means changing the position of the elements in array itself.
from numpy import random
import numpy as np
arr=np.array([2,3,4,5])
random.shuffle(arr)
print(arr)

#generating permutation of arrays
arr1=np.array([3,4,5,6,8])
print(random.permutation(arr1))
#Note: permutation() method return a re-arranged array and leaves the original array unchanged.