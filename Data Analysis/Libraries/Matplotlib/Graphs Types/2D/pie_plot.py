import matplotlib.pyplot as plt
import numpy as np

game_of_the_year = ["Red Dead Redemption 2", "God of War: Ragnarok", "Elden Ring", "Resident Evil 4", "Lies of P"]
votes = np.random.random(5) * 100
explodes = [0.0, 0.0, 0.2, 0.0, 0.0] # parameter used to pull out one/multiple parts of the chart

plt.pie(votes, labels=game_of_the_year, autopct='%1.2f%%', explode=explodes) # 'labels' is a statement required for it to work, this one is not like the other graphs
plt.show()