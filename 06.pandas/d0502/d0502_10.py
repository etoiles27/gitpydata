import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')



df['학교']=df['학교']+'등학교'
df['키']=df['키'].astype(str) + 'cm'
print(df.columns)






print(df)

