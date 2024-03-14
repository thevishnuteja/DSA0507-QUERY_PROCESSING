import pandas as pd
import numpy as np
df=pd.read_csv(r"E:/DS-1/sales.csv")
table=pd.pivot_table(df,index='Item',values='Sale_amt',aggfunc=[np.max,np.min])
print(table)
