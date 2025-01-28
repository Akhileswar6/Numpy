#Seaborn
#Seaborn module is a library that uses matplotlib underneath to plot graphs.

import matplotlib.pyplot as plt
import seaborn as sns

#Distplots-> stands for distribution plots and it takes as input an array and plots a curve corresponding to the distribution of points in array.

#plotting a Distplot
sns.distplot([23,45,67,89,56])
plt.show()

#plotting a dsitplot with bins
sns.distplot([23,45,67,89,56],bins=5)
plt.show()

#plotting a distplot without histogram
sns.distplot([0,3,4,5,7], hist=False)
plt.show()

