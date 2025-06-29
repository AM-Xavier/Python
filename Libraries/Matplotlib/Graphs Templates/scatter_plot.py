import matplotlib.pyplot as plt
import numpy as np

x = np.random.random(20) * 100
y = np.random.random(20) * 100

plt.scatter(x, y, c='purple')
plt.show()