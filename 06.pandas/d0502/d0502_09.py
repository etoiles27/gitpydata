import pandas as pd


df = pd.read_excel('인구통계2.xls')


df['총인구수'] = df['2021년_남자 인구수']+df['2021년_여자 인구수']
df['도시'] = '중도시' 
filt1 = df['총인구수']>5000000
filt2 =( df['총인구수']<5000000) & (df['총인구수']>500000)
df.loc[filt2, '도시'] = '소도시' 
df.loc[filt1, '도시'] = '대도시' 


df.loc['합계'] = [0, df['2021년_세대수'].sum(),df['2021년_남자 인구수'].sum(),df['2021년_여자 인구수'].sum(),df['총인구수'].sum(),0]


print(df.columns)
print(df)