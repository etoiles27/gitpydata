import pandas as pd
import re

from pyparsing import col
df_m = pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관',usecols='B,E:Y')
df_w = pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관',usecols='B,AB:AV')

# 컬럼이름 한번에 바꾸기 
df_w.columns = df_m.columns
# print(df_w.columns)

# rename
# df_w.rename(columns={df_w.columns[0]:re.sub('[^0-9~]','',df_w.columns[0])},inplace=True)
# df_w.rename(columns={'0~4세':'4세'},inplace=True)

print(len(df_w.index[0]))

df_w.rename(index={df_w.index[0]:(df_w.index[0].strip())},inplace=True)

print(len(df_w.index[0]))



print(re.sub('[ㄱ-힣]','',df_w.columns[0]))


# print(df_w.index.values)
# print(df_w[df_w.columns[0]])

# print(df['0~4세'])
# print(df['0~4세'][0])
# print(type(df['0~4세'][0]))


# print(re.sub('[^0-9]','',df['0~4세'][0]).astype(int))

# df.values =  re.sub('[^0-9~]','',df.values)

# print(df)