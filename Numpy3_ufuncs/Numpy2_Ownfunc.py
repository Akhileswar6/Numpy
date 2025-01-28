#Create your own ufunc

import numpy as np
def myadd(x,y):
    return x+y
myadd=np.frompyfunc(myadd,2,3)
print(myadd([1,2,3,4], [4,5,6,7]))

#check if a function is a ufunc
print(type(np.add))
print(type(np.concatenate))

#print(type(np.akhil))

if type(np.add) == np.ufunc:
    print("add is func")
else:
    print("add is not ufunc")
    