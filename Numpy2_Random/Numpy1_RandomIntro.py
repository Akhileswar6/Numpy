#Random numbers in numpy

from numpy import random
x=random.randint(100)
print(x)

#Generate random float
y=random.rand()
print(y)

#Generate random arrayy
#integers
x1=random.randint(100,size=(5))
print(x1)

#2-D array
x2=random.randint(1000, size=(4,5))
print(x2)

#floats
x3=random.rand(10)
print(x3)

#2-D array
x4=random.rand(4,6)
print(x4)

#generate random number from array
#choice-> this method allows you to generate a random value based on array valoues
x5=random.choice([34,45,56,7])
print(x5)

#2-D array 
#randomly selects the from the array and convert it into 2-d array
x6=random.choice([3,4,5,98],size=(3,5))
print(x6)

