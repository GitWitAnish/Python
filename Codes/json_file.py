
# JSON stands for JavaScript Object Notation.
# Actually, it is a stringified JavaScript object or Python dictionary.

# dictionary
person_dct= {
    "name":"Anish",
    "country":"Nepal",
    "city":"Pokhara",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Anish', 'country': 'Nepal', 'city': 'Pokhara', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Anish",
    "country":"Nepal",
    "city":"Pokhara",
    "skills":["JavaScrip", "React","Python"]
}'''




#Changing JSON to Dict

import json
person_json = '''{
    "name":"Anish",
    "country":"Nepal",
    "city":"Pokhara",
    "skills":["JavaScript", "React","Python"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])











#csv extension

# CSV stands for comma separated values.
# CSV is a simple file format used to store tabular data, such as a spreadsheet or database. 
# CSV is a very common data format in data science.




#xlsx extension
#To read excel files we need to install xlrd package




