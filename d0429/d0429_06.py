import pandas as pd


# df = pd.read_excel('user.xlsx')


# print(df.columns)
# print(df.index.values)


# print(df.loc[499:599,['first_name','email']])

df = pd.read_excel('user.xlsx',index_col='id')

# # print(df)
# print(df.iloc[499:600])
# print(df.loc[500:600,['first_name','email']])


# print(df.iloc[(df.index>=500) & (df.index<=600)  | (df.index==605)])


# # print(df.loc[500:600 | (df.index==605)])

# print(df.loc[(df.index>=500) & (df.index<=600)  | (df.index==605)])


# print(df.loc[(df.index>=500) & (df.index<=600)  | (df.index==605), ['first_name','email']])

print(df.iloc[(df.index>=500) & (df.index<=600)  | (df.index==605), [0,2]])




cond1 = (df.index>=500) & (df.index<=600)  | (df.index==605)
cond2 = df['gender'] =='Male' 

print(df.loc[cond1  & cond2, ['first_name','email']])

# df.set_index('gender',inplace=True)
# print(df.index.values)
# print(df.loc[df.index =='Male',['first_name','email']])



