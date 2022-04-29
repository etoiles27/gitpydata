import pandas as pd
import numpy as np



df = pd.read_excel('score.xlsx',index_col='지원번호')
# 결축치 : Nan 데이터 처리
# print(df.fillna('없음'))

# df['학교'] = np.nan
# df['학교'] = '없음'

# df['수학'].fillna(0,inplace=True)
df.fillna('없음',inplace=True)

df.dropna(inplace=True)
print(df)
