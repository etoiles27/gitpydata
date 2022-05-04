import pandas as pd

df = pd.read_excel('score.xlsx',index_col='지원번호')


# print(df.groupby('학교').mean())

print(df.index)
print(df.columns)

df['학년'] = [3,3,2,1,1,3,2,2]

# 1개 그룹 
# print(df.groupby('학교').count())

# 2개 그룸화

print(df.groupby(['학교','학년']).mean())


print(df.groupby(['학년']).mean().sort_values('키',ascending=False))










print(df)