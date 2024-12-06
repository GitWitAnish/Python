# Lambda function is a small anonymous function without a name.
#  It can take any number of arguments, but can only have one expression.
#  Lambda function is similar to anonymous functions in JavaScript.



#To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression. 
# See the syntax below. 
# Lambda function does not use return but it explicitly returns the expression.

# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))



# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22



