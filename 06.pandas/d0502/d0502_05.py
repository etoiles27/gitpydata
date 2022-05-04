import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')


# # 컬럼 삭제. df.drop(columns)
# df.drop(columns=['국어'],inplace=True)
# df.drop(columns=['과학','사회'],inplace=True)

# # row 삭제
# df.drop(index='3번',inplace=True)
# df.drop(index=['1번','3번'],inplace=True)


# filt = df['수학'] >= 80
# df.drop(index = df[filt].index ,inplace=True)


print(df)