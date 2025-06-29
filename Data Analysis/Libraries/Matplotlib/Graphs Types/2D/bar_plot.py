import matplotlib.pyplot as plt
import numpy as np

device_brands = ['Samsung', 'Apple', 'Nokia', 'Google', 'Motorola', 'LG']
user_numbers = np.random.random(6) * 100

plt.bar(device_brands, user_numbers, color='red', width=1, edgecolor='white')
plt.show()