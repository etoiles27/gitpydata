import pandas as pd

df = pd.read_excel('연령별인구현황_월간.xlsx',skiprows=3,usecols='B,AB:AV')


df.set_index('행정기관',inplace=True)

print(df)

# print(df.columns[-1])
print(df[df.columns[-1]][1:].str.replace(',','').astype(int).sum())
m = df[df.columns[-1]][1:].str.replace(',','').astype(int).sum()
print('{:,d}'.format(m))


# print(df.columns)

# df.columns = ['0~4', '5~9', '10~14', '15~19', '20~24', '25~29','30~34', '35~39', '40~44', '45~49', '50~54', '55~59','60~64', '65~69', '70~74', '75~79', '80~84', '85~89','90~94', '95~99', '100~']

# print(df.columns)

# print(df['행정기관'])

df.rename(index={'전국  ':'전국'},inplace=True)

print(df.index)