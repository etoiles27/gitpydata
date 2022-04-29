import pandas as pd


# df = pd.read_excel('user.xlsx',index_col=0)
# print(df.iloc[550:560])

# df = pd.read_excel('stat_142801.xls',skiprows=2,nrows=2)
# print(df['2020'])
# print(df[df.columns[-1]])



df = pd.read_excel('score.xlsx',index_col='지원번호')
# df.set_index('이름',inplace=True)
# # print(df.iloc[2])
# # print(df.loc['강태원'])
# print(df.index)
# print(df.loc[df.index[0]])
# print(df.columns[6:-1])
# print(df[df.columns[6:-1]])
print(df.describe())

print('키 최소값 :',df['키'].min())
print('키 최소값 :',df['키'].max())
print(df['키'].nlargest(3))
print(df['키'].nsmallest(5))


print(df['학교'].unique())