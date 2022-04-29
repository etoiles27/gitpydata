import pandas as pd
import re

df = pd.read_excel('score.xlsx',index_col='지원번호')

# print(df)


print(df.loc['1번','국어'])
print(df.loc[['1번','2번'],['국어','영어']])


print(df.loc['1번':'5번','국어'])
print(df.loc['1번':'5번','국어':'사회'])

