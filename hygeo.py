import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ngood, nbad, nsamp = int(input("input no of good")), int(input("input no of bad")), int(input("input no of samples"))
s = np.random.hypergeometric(ngood, nbad, nsamp, 1000)
sns.distplot(s, kde=False)

plt.show()
