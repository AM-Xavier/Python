import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

device_brands = ['Samsung', 'Apple', 'Nokia', 'Google', 'Motorola', 'LG']
user_numbers = np.random.random(6) * 100

fig.suptitle('Number of users on each device', fontsize=14, fontweight='bold')

ax.set_xlabel('Devices', fontsize='11')
ax.set_ylabel('Number of users', fontsize='11')


plt.bar(device_brands, user_numbers, color='red', width=1, edgecolor='white')
plt.show()