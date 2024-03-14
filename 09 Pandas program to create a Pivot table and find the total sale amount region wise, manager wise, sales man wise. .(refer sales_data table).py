import numpy as np
import pandas as pd
df = pd.read_csv("E:\DS-1\sales.csv")
print(pd.pivot_table(df,index=["Region","Manager","SalesMan"],values="Sale_amt",aggfunc=np.sum))
