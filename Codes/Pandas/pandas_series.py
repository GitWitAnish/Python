import pandas as pd
import numpy as np

#Creating Pandas Series with Default Index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

    # 0    1
    # 1    2
    # 2    3
    # 3    4
    # 4    5
    # dtype: int64  









#Creating Pandas Series with custom index

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)


    # 1    1
    # 2    2
    # 3    3
    # 4    4
    # 5    5
    # dtype: int64






#Creating Pandas Series from a Dictionary

dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)


    # name       Asabeneh
    # country     Finland
    # city       Helsinki
    # dtype: object









#Creating a Constant Pandas Series


s = pd.Series(10, index = [1, 2, 3])
print(s)

    # 1    10
    # 2    10
    # 3    10
    # dtype: int64







#Creating a panda series using linspace

s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

