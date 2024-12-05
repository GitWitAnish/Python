

# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.



#Creating dict
# To create a dictionary we use curly brackets, {} or the dict() built-in function.

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}




# The dictionary below shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.
person = {
    'first_name':'Anish',
    'last_name':'Karki',
    'age':250,
    'country':'Nepal',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Lamjung',
        'zipcode':'33600'
    }
    }




#Accessing dict 
print(person['first_name']) # Anish
print(person['country'])    # Nepal
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Lamjung
print(person['city'])       # Error



#Adding items to dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


#Modifying items in dict
person['first_name'] = 'Guts'
person['age'] = 252

