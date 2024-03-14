import pandas as pd
employees=pd.read_csv(r"E:\DS-1\dept.csv")
print("Distinct department_id:")
print(employees.DEPARTMENT_ID.unique())
