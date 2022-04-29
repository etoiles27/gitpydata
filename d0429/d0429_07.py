import pandas as pd
import re

df = pd.read_excel('score.xlsx',index_col='지원번호')

print(df['키']>180)

filt1 = df['키'] > 188 
filt2 = df['학교'] == '구로고'
print(df[filt1])

print(df[~(df['키']>190)])



print(df.loc[filt1 & filt2,'이름':'사회'])