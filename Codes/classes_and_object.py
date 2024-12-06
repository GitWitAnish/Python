class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Anish', 'Karki', 250, 'Nepal', 'Pokhara')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)