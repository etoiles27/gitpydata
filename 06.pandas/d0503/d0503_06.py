import pandas as pd


df = pd.read_csv('전체연봉.csv',encoding='utf-8-sig')

filt = df['WAR'].isnull()

df.loc[filt,'WAR']=0
# df['WAR'].fillna(0,inplace=True)
# print(df[filt])
# filt2 = (df['선수']=='애플러') & (df['연도']==2022 )
# print(df[filt2])

# print(df.groupby('선수').mean())

# print(df.sort_values('선수'))

print(df.groupby('팀')['연봉(만원)'].mean())
print(df.groupby('팀').count())