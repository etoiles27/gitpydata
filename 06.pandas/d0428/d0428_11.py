

import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')
# print(df.columns)
# print(df.columns[0])
# print(df.columns[2])
# print(df['이름'])
print(df.columns[[1,5]])


print(df[df.columns[[1,5,-1]]])
print(df[df.columns[1:4]])


print(df['영어'])
print(df['영어'][0:2])