import pandas as pd
import numpy as np

df = pd.read_excel('score.xlsx',index_col='지원번호')

# print(df.sort_index())
# print(df.sort_index(ascending=False))
# print(df.sort_values('키'))
# print(df.sort_values('키',ascending=False))


print(df.sort_values(['수학','영어'],ascending=[False,True]))