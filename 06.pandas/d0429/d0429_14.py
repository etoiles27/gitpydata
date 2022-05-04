from re import A
import pandas as pd

# df = pd.read_excel('시가총액1-200.xlsx')

# print(df)

# print(df.columns)
# print(df.sort_values(['종목명']))


df = pd.read_excel('user.xlsx')

# print(df)

# print(df.columns)

# print(df.sort_values(['first_name']))
# print(df.sort_values(['gender','first_name'],ascending=[True,False]))

print(df['gender'].unique())