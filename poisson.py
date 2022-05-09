from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
float(input("input value of lamda"))
sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()