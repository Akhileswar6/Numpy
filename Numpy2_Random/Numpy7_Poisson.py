#Poisson Distribution
#It estimates how many times an event can happen in a specified time.

#it has two parameters:
#lam-> rate or known number of occurrences
#size-> The shape of the returned array.

from numpy import random
x=random.poisson(lam=2, size=10)
print(x)

#visualizing poisson distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

#Difference between Poisson and Normal Distribution
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label="normal")
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label="Poisson")
plt.show()