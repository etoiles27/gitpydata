import pandas as pd


df = pd.read_excel('movie.xlsx')

print(df)
print(df.values)
print(df.index.values)
print(df.loc[1])
# print(df.columns)

print(df.iloc[0:2])





# print('총 관객 수 : ', df['관객 수'].sum())
# print(df[df.columns[[0,2]]])
# print('최대 관객 수 : ', df['관객 수'].max())
# #  영화 개봉연도 3개
# print(df[df.columns[0:1]][0:3])




















# df = pd.read_excel('시가총액1-200.xlsx')
# print(df.columns)

# print(df['N'])
# print(df.columns[0])

# df.set_index(df.columns[0],inplace=True)
# print(df)
# print(df.loc['삼성전자'])



# df.index.name='번호'
# # print(df.index)
# df.reset_index(inplace=True)
# df.set_index('번호',inplace=True)

# print(df.columns)
# print(df['번호'])


