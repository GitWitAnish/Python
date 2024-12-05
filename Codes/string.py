# Single line 

a = 'ANISH'
print(a)


# Multiple line

a = ''' My name is Anish Karki.
 I am a Computer Engineer.  '''
print(a)


# String Concatenation
first_name = 'Anish'
last_name = 'Karki'
space = ' '
full_name = first_name  +  space + last_name
print(full_name)


# Checking length of a string using len() builtin function
print(len(first_name)) 

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o



# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon



# capitalize(): Converts the first character the string to Capital Letter

challenge = 'coding is fun.'
print(challenge.capitalize()) # 'Coding is fun.'


# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`





# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0



# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # type: ignore # True