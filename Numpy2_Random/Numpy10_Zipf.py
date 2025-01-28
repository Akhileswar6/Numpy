#Zipf Distribution
#It is used to sample data based on Zipf's law.

#it has two parameters:
#a-> distribution parameter.
#size->The shape of the returned array.

from numpy import random
x=random.zipf(a=2, size=(2,3))
print(x)

#visualizing zipf distribution
import matplotlib.pyplot as plt
import seaborn as sns
x=random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show()