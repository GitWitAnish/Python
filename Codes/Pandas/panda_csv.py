#Reading CSV File Using Pandas

import pandas as pd

df = pd.read_csv('../Python/Codes/Pandas/weight-height.csv')
print(df)




#read only the first 5 rows using head()

print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method





#last recordings of the dataframe using the tail() methods.

print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method





#Shape of csv file 
print(df.shape)   #(10000, 3)



print(df.columns)     #Index(['Gender', 'Height', 'Weight'], dtype='object')






#To get specific column

heights = df['Height'] # this is now a series
print(heights)







weights= df['weight']
print(len(heights) == len(weights))   #TRUE









#describe() method provides a descriptive statistical values of a dataset.

print(heights.describe()) # give statisical information about height data

    # count    10000.000000
    # mean        66.367560
    # std          3.847528
    # min         54.263133
    # 25%         63.505620
    # 50%         66.318070
    # 75%         69.174262
    # max         78.998742
    # Name: Height, dtype: float64













#MODIFYING A DATAFRAME


import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)


#Adding a column

weights = [74, 78, 69]
df['Weight'] = weights
print(df)


# 	Name	Country	City	Weight
# 0	Asabeneh	Finland	Helsinki	74
# 1	David	UK	London	78
# 2	John	Sweden	Stockholm	69


#Modifying column values

df['Height'] = df['Height'] * 0.01
print(df)



