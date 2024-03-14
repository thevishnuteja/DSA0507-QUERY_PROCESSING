import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"E:\DS-1\Alphabet Stock.csv")
start_date=pd.to_datetime('2020-4-1')
end_date=pd.to_datetime('2020-4-30')
df['Date']=pd.to_datetime(df['Date'])
new_df=(df['Date']>=start_date)&(df['Date']<=end_date)
df1 =df.loc[new_df]
df2 = df1.set_index('Date')
plt.figure(figsize=(6,6))
plt.suptitle('Trading Volume of Alphabet Inc. stock,\n01-04-2020 to 30-04-2020',fontsize=16,color='black')
plt.xlabel("Date",fontsize=12,color='black')
plt.ylabel("Trading Volume",fontsize=12,color='black')
df2['Volume'].plot(kind='bar');
plt.show()
