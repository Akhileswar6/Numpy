#Numpy Hyperbolic functions
#NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..

import numpy as np
x=np.sinh(np.pi/2)
print(x)

arr=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
x1=np.cosh(arr)
print(x1)

#finding angles
x2=np.arccosh(1.0)
print(x2)

#Angles of each values in array
arr1=np.array([1,0.1,0.2])
x3=np.arctanh(arr1)
print(x3)
