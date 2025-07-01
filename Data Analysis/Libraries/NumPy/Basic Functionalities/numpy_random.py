import numpy as np


# Generating a random number
number = np.random.randint(101) # this will generate a random number from 0-100
print(number)
print()

numbers = np.random.randint(101, size=(2,3,4)) # you can also use this function to generate an array by specifying the size
print(numbers)                 #(array, row, columns)
print()

numbers = np.random.randint(91, 101, size=(2,3,4)) # you can also specify a range
print(numbers)
print()

# Generating the results of a Binomial Distribution
coin_flip = np.random.binomial(1, p=0.5, size=(5,10)) # this uses an int
print(coin_flip)            # (trials, probability, size)
print()

# Generating the results of a Normal Distribution
normal = np.random.normal(loc=1.65, scale=0.15, size=(5,10)) # this uses a float
print(normal)          # (mean, standard deviation, size)
print()
print(np.round(normal, 2))