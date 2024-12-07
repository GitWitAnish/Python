import numpy as np


# Generate a random float  number
random_float = np.random.random()
print(random_float)


random_floats = np.random.random(5)
print(random_floats)       #[0.35961285 0.63999396 0.93463488 0.14269954 0.97712236]






# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
print(random_int)           #[4 8 7 9]



random_int = np.random.randint(2,10, size=(3,3))
print(random_int)











 # np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
normal_array

# mu = 79: This is the mean (average value) of the distribution.
# sigma = 15: This is the standard deviation, which measures the spread of values around the mean.
# size = 80: This specifies generating 80 random numbers.






