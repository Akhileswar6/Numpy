#Random data distribution
#the probability is set ny number between 0 and 1, where 0 means that value will never occur and 1 means that the value will always occur.

from numpy import random
x=random.choice([3,5,7,98], p=[0.1,0.3,0.6,0.0],size=(10))
print(x)

x1= random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x1)