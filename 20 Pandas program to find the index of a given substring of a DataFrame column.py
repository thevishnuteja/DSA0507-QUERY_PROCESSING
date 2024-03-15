import pandas as pd
df=pd.DataFrame({
'name_code':['c0001','1000c','b00c2','b2c02','c2222'],
'date_of_birth ':['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
'age':[18.5,21.2,22.5,22,23]})
print("Original DataFrame:")
print(df)
print("\nIndex of a substring in a specified column of a dataframe:")
df['Index']=list(map(lambda x:x.find('c',0,5),df['name_code']))
print(df)
