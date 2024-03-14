import pandas as pd
jobs=pd.read_csv(r"E:\DS-1\job.csv")
result=jobs.sort_values('JOB_TITLE')
for index, row in result.iterrows():
    print(row['JOB_ID'].ljust(15),row['JOB_TITLE'].ljust(35),str(row['MIN_SALARY']).ljust(9),row['MAX_SALARY'])
