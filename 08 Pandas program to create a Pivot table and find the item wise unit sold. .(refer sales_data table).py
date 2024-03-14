import pandas as pd
import numpy as np
df=pd.read_csv("E:\DS-1\sales.csv")
print(pd.pivot_table(df,index=["Item"],values="Units",aggfunc=np.sum))
