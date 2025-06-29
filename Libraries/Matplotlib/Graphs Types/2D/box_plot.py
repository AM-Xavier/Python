import matplotlib.pyplot as plt
import numpy as np


heights_in_centimeters = np.random.normal(170, 8.5, 200)

plt.boxplot(heights_in_centimeters, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "white", "linewidth": 0.5},
                boxprops={"facecolor": "C0", "edgecolor": "white", "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 1.5},
                capprops={"color": "C0", "linewidth": 1.5}) # some alignment and color code i got from matplotlib documentation to make it blue
plt.show()