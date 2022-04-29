import pandas as pd


# df = pd.read_excel('user.xlsx',index_col=0)

# df = pd.read_excel('user.xlsx',skiprows=[i for i in range(0,500)],nrows=10)
df = pd.read_excel('score.xlsx',index_col='지원번호')
# df=pd.read_csv('googlemovie.csv')

# 숫자컬럼 통계를 보여준다 
# print(df.describe())

# print(df.info())
# print(df.head(10))
# # 하위 10줄을 보여준다
# print(df.tail(10))
# # 0번째 row출력
# print(df.iloc[0])
# # index 출력
# print(df.index)
# #컬럼출력
# print(df.columns)
# # row 와 col 수
# print(df.shape)
# print(df[['first_name','last_name']])
# # 배열구조 출력

# print(df.values)
# print(df.values[0:5])


print(df.index)
print(df.index[3])
print(df.iloc[0])
print(df.loc['3번'])


# print(df)

