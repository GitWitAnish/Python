
#Creating a module named mymodule and importing it in main.py



from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g


print(fullname('Anish','Karki'))
print(total(1, 9))

mass = 100
weight = mass * g
print(weight)

print(p)
print(p['firstname'])