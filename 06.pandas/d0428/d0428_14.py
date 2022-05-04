from matplotlib import use
import pandas as pd

df = pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3,usecols='B,E:Y')


df.set_index('행정기관',inplace=True)



# print(df.loc[df.index[1]])

# print(df.columns)
# print(df.index)

# print(df.loc[df.index[0]])

print(df.index.values)
print(df.columns)

print(df.info)

# print(df[df.columns[0]].sum())

print(df['0~4세'][1:].str.replace(',','').astype(int).sum())

print(df.iloc[0:2])

print(df.loc)