import pandas as pd
import numpy as np

df = pd.read_excel('score.xlsx',index_col='지원번호')

# df.dropna(axis='index', inplace=True)
# df.dropna(axis='columns', inplace=True)




df['학교']=np.nan
# df.dropna(axis='columns',how='any', inplace=True)
df.dropna(axis='columns',how='all', inplace=True)
print(df)