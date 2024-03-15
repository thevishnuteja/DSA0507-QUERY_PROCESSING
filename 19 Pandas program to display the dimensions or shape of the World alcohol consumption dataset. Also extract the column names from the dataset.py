import pandas as pd
wcon=pd.read_csv("E:/DS-1/drinks.csv")
print("World alcohol consumption sample data:")
print(wcon.head())
print('\nShape of the dataframe: ',wcon.shape)
print('\nNumber of rows: ',wcon.shape[0])
print('\nNumber of column: ',wcon.shape[1])
print("\nExtract Column Names:")
print(wcon.columns)
