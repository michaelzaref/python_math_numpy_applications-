import numpy as np
import matplotlib.pyplot as plt
X=float(input("input x"))
t=int(input("input t"))
gfg = np.random.geometric(X,t)

count, bins, ignored = plt.hist(gfg, 40, density=True)
plt.show()