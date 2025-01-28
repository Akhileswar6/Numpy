#Numpy ufuncs
#ufuncs stands for universal functions.

x=[2,3,3,4]
y=[1,2,3,4]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)

import numpy as np
x=[2,3,3,4]
y=[887,8,78,9]
z=np.add(x,y)
print(z)