import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')


print(df.groupby('학교').get_group('구로고'))

print(df.groupby('학교').mean())
print(df.groupby('학교').size())
print(df.groupby('학교').size()['구로고'])


print(df.groupby('학교').mean()['키'])
print(df.groupby('학교')['키'].mean())



print(df.groupby('학교')[['키','영어']].mean())