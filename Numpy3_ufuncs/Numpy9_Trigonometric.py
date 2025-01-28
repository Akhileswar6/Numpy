#Numpy trigonometric functions
#NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values

import numpy as np
x=np.sin(np.pi/2)
print(x)

arr=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
x1=np.sin(arr)
print(x1)

#convert degrees into radians
arr1=np.array([90,180,270,360])
x2=np.deg2rad(arr1)
print(x2)

#convert radians into degrees
arr2=np.array([np.pi/2,np.pi,1.5*np.pi, 2*np.pi])
x3=np.rad2deg(arr2)
print(x3)

#finding angles
arr3=np.arcsin(1.0)
print(arr3)

#angles of each values in array
arr4=np.array([1,-1,0.1])
x=np.arccos(arr4)
print(x)

#hypotenues
base=3
perp=4
x=np.hypot(base,perp)
print(x)
