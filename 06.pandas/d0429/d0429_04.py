import pandas as pd

df = pd.read_excel('gmovie.xlsx')#,index_col='제목')

# df.to_excel('gmovie.xlsx')

print(df)

#4,5 ->제목 가격
print(df.loc[3:4,['제목','가격']])


df.loc[3:4,'가격'] = 1000 
print(df.loc[3:4,['제목','가격']])