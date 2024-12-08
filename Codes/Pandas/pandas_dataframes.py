import pandas as pd



#Creating Dataframe from list of lists

data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

#       Names  Country       City
# 0  Asabeneh  Finland    Helsink
# 1     David       UK     London
# 2      John   Sweden  Stockholm








#Creating Dataframe using Dictionary


data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)



# 	Name	Country	City
# 0	Asabeneh	Finland	Helsiki
# 1	David	UK	London
# 2	John	Sweden	Stockholm













#Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# 	Name	Country	City
# 0	Asabeneh	Finland	Helsinki
# 1	David	UK	London
# 2	John	Sweden	Stockholm

















