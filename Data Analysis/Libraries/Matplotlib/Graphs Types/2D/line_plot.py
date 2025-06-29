import matplotlib.pyplot as plt
import numpy as np

years = [2000 + x for x in range(10)]
ages = np.random.normal(20, 2.5, 10)

plt.plot(years, ages, c='red')
plt.show()