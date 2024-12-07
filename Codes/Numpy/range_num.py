import numpy as np

# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

natural_numbers = np.arange(1, 20, 1)
natural_numbers

odd_numbers = np.arange(1, 20, 2)
odd_numbers

even_numbers = np.arange(2, 20, 2)
even_numbers






# numpy.linspace()

# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
np.linspace(1.0, 5.0, num=10)    #    array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778, 3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])





# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

np.logspace(2, 4.0, num=4)    # array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])





