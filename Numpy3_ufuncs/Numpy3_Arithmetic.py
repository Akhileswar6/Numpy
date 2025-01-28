#simple Arithmetic

#addition
import numpy as np
arr1=np.array([1,2,3,87,82])
arr2=np.array([23,19,20,30,39])
newarr=np.add(arr1,arr2)
print(newarr)

#Subtract
arr3=([23,45,67,89])
arr4=([98,76,54,32])
newarr1=np.subtract(arr3,arr4)
print(abs(newarr1))

#Multiply
arr5=([76,98,36,53])
arr6=([98,65,83,28])
newarr2=np.multiply(arr5,arr6)
print(newarr2)

#Division
arr7=([98,76,54,32])
arr8=([23,45,67,89])
newrarr3=np.divide(arr7,arr8)
print(newrarr3)

#power
arr9=([2,3,4,5])
arr10=([2,5,6,7])
newarr4=np.power(arr9,arr10)
print(newarr4)

#remainder
arr11=([23,45,67,89])
arr12=([98,76,54,32])
newarr5=np.remainder(arr11,arr12)
newarr6=np.mod(arr11,arr12)
print(newarr5)

#quotient and mod
arr13=([23,45,67,89])
arr14=([98,76,54,32])
newarr7=np.divmod(arr13,arr14)
print(newarr7)

#absolute
arr15=([-23,-45,67,-89])
newarr8=np.absolute(arr15)
print(newarr8)