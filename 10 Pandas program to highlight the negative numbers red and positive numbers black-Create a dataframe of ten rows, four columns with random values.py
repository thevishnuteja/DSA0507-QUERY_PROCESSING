import pandas as pd
import numpy as np
np.random.seed(24)
df=pd.DataFrame({'A':np.linspace(1,10,10)})
df=pd.concat([df,pd.DataFrame(np.random.randn(10,4), columns=list('BCDE'))], axis=1)
print("Original array:")
print(df)
def color_negative_red(val):
    color='red' if val<0 else 'black'
    return'color: %s'%color
print("\nNegative numbers red and positive numbers black:")
styled_df = df.style.map(color_negative_red)
print(styled_df)
