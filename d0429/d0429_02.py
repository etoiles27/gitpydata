from os import rename
import pandas as pd
import re

df = pd.read_excel('stat_142801.xls',skiprows=2,skipfooter=2)

# df.index.name='목록'
# df.reset_index(inplace=True)

# df.columns[0] = '목록'

df.rename(columns={'Unnamed: 0':'목록'},inplace=True)
df.set_index('목록',inplace=True)

# print(df.columns)
# print(df.iloc[df.columns[0:3]])

print(df.index.values)
df.rename(index={df.index[0]:re.sub(r'[^ㄱ-힣]','',df.index[0])},inplace=True)
df.rename(index={df.index[1]:re.sub(r'[^ㄱ-힣]','',df.index[1])},inplace=True)
print(df.index.values)

print(df.loc[df.index[0]][0:3])

