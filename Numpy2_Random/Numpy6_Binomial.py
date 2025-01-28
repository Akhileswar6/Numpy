#Binomial Distribution

#It describes the outcome of binary scenarios, eg. toss of a coin, it will either be head or tails.
#It has three parameters:
#n->number of trials.
#p->probability of occurence of each trial.
#size->The shape of the returned array.

from numpy import random
x=random.binomial(n=10, p=0.5, size=10)
print(x)

#visualizing binomial distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

#Difference between normal and binomial distribution
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label="normal")
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label="binomial")
plt.show()