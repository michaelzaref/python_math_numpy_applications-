import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
n, p = int(input("input no. of success")), float(input("input propability of success"))
s = np.random.negative_binomial(n, p, 100000)

sns.distplot(s, kde=False)

plt.show()