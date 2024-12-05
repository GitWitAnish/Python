

#  We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).

# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple



# syntax
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple length
tpl = ('item1', 'item2', 'item3')
print(len(tpl))


#Accessing tuple 
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]


#Slicing tuple 
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]



#Changing tuple to list 
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')


#Joining tuple 
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables



#Deleting tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits



