import pandas as pd

# # csv읽어오기
# df = pd.read_csv('score.csv',index_col='지원번호')

# # csv읽어오기
# df = pd.read_csv('score.txt',sep=',',index_col='지원번호')


# # excel읽어오기
# df = pd.read_excel('score.xlsx',index_col='지원번호')



# 첫번째 행을 잘라내고 가져오기

# df = pd.read_excel('stat_142801.xls',skiprows=[0,1,3,5],index_col=0)




df = pd.read_excel('user.xlsx',skiprows=[0,1,3,5],index_col=0)











print(df)
# print(df.index)
# print(df.iloc[0])