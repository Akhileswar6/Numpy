#Normal (Gaussian) Distribution
#It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

#it has three parameters:
#loc->(Mean)->where the peak of the bell exists.
#scale->(Standard deviation)->how flat the graph distribution should be.
#size->The shape of the returned array.

from numpy import random
x=random.normal(size=(2,3))
print(x)

x1=random.normal(loc=1, scale=2, size=(2,3))
print(x1)

#visualizing normal distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000), hist=False)
plt.show()