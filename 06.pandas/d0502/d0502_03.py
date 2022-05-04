import pandas as pd

df = pd.read_excel('2020년월별교통사고01.xlsx',skiprows=2,index_col='월')

print(df.columns)


df['교통사고 피해수(명)']=df['사망자수(명)']+df['부상자수(명)']

df.loc['합계'] = [0,0,0,0]
df.loc['평균'] = [0,0,0,0]


df.loc[['합계','평균'],'사고건수(건)'] = [df['사고건수(건)'].sum(),(df['사고건수(건)'].sum()/12)]
df.loc[['합계','평균'],'사망자수(명)'] = [df['사망자수(명)'].sum(),(df['사망자수(명)'].sum()/12)]
df.loc[['합계','평균'],'부상자수(명)'] = [df['부상자수(명)'].sum(),(df['부상자수(명)'].sum()/12)]
df.loc[['합계','평균'],'교통사고 피해수(명)'] = [df['교통사고 피해수(명)'].sum(),(df['교통사고 피해수(명)'].sum()/12)]

print(df)

# 평균보다 낮은 row 값 삭제. 

filt = df['사고건수(건)'] <= df.loc['평균','사고건수(건)']
df.drop(index = df[filt].index ,inplace=True)
print(df)


# 사망자수가 230 미만 삭제
filt2 = df['사망자수(명)']<230
df.drop(index = df[filt2].index ,inplace=True)
print(df)
