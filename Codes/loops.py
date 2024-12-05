
#while loop
a = 0
while a < 5:
    print(a)
    a = a + 1    #prints from 0 to 4
else:
    print(a)



#break and continue
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break


count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1


#for loop 
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])




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


for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out



#range() function
#range(start, end, step)

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}






for number in range(11):
    print(number)   # prints 0 to 10, not including 11




#Nested for loop

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


for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)



#for else

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)




