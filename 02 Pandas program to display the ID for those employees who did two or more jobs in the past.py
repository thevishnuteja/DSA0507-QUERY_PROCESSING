import pandas as pd
employees=pd.read_csv(r"E:\DS-1\emp.csv")
result=employees.groupby(['EMPLOYEE_ID'])
print(result.filter(lambda x:len(x)>1).groupby('EMPLOYEE_ID').size().sort_values(ascending=False))
