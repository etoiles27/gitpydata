import pandas as pd


df = pd.read_excel('score.xlsx',index_col='지원번호')



print(df.values)

print(df.loc['1번']) 
print(df.loc[df.index[0]])

print(df.iloc[1])
print(df.iloc[0:2])


