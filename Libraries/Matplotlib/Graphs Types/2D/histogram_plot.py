import matplotlib.pyplot as plt
import numpy as np

ages = np.random.normal(15, 1.5, 1000)

plt.hist(ages, bins=10)
plt.show()