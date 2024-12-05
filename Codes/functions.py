

#functions without parameter

def generate_full_name ():
    first_name = 'Anish'
    last_name = 'Karki'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function



#function returning the value

def generate_full_name ():
    first_name = 'Anish'
    last_name = 'Karki'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())



#function with parameter

def intro(name):
    message = "My name is " + name + "."
    return message

print(intro("Anish"))



#function with multiple parameter

def intro(first_name , last_name):
    message = "My name is" + " "+ first_name +" "+ last_name + "."
    return message

print(intro("Anish" , "Karki"))



#function with default parameter

def intro(name = "Anish"):
    message = "My name is " + name + "."
    return message
print(intro())