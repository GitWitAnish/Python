import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())
# This code reads a CSV file named 'data.csv', removes any rows with empty cells, and prints the resulting DataFrame.





df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)
# Replace NULL values with the number 130


