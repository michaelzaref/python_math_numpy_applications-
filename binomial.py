from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x=int(input("input x"))
y=float(input("input y"))
z=int(input("input z"))
sns.distplot(random.binomial(x, y,z), hist=True, kde=False)

plt.show()