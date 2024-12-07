


#Addition

import numpy as np


num = np.array([1,2,3,4,5])
print(num)    #[1 2 3 4 5]

plus_ten = num + 10

print(plus_ten)    #[11 12 13 14 15]





#Substraction

num = np.array([1,2,3,4,5])
print(num)    #[1 2 3 4 5]

minus_ten = num - 10

print(minus_ten)    #[-9 -8 -7 -6 -5]





#Multiplication


num = np.array([1,2,3,4,5])
print(num)    #[1 2 3 4 5]

multiply_ten = num * 10

print(multiply_ten)    #[10 20 30 40 50]
                  




#Division


num = np.array([1,2,3,4,5])
print(num)    #[1 2 3 4 5]

divide_ten = num / 10

print(divide_ten)    #[0.1 0.2 0.3 0.4 0.5]




# remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
remainder = numpy_array_from_list % 3
print(remainder)








# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)



# Let's break down the // (floor division) operator with clear examples:

# How // Works:
# It divides two numbers.
# It rounds down the result to the nearest integer (toward negative infinity).

# print(10 // 3)  # 10 divided by 3 is 3.33, rounds down to 3
# print(20 // 4)  # 20 divided by 4 is 5.0, so the result is 5
# print(15 // 2)  # 15 divided by 2 is 7.5, rounds down to 7









#Exponential


num = np.array([1,2,3,4,5])
print(num)    #[1 2 3 4 5]

exponential = num ** 2

print(exponential)    #[ 1  4  9 16 25]
                    