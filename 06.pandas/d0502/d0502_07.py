import pandas as pd


df = pd.read_excel('user.xlsx',index_col='id')

df['total'] = 0

print(df)


cond1 = ((df.index>=601) & (df.index<=700) ) | (df.index==500) | (df.index==505)  | (df.index==910) | (df.index==950) 
df.loc[cond1]['total'] = 100

print(df.loc[cond1])  

print()