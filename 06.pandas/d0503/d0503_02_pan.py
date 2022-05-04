import pandas as pd

df = pd.read_csv('daummovies.csv',encoding='utf-8-sig')
df.index.name='영화번호'
df.reset_index(inplace=True)
df.set_index('영화번호',inplace=True)


df['추천점수'] = (df['누적인원']*df['평점'])/100

# 2. pandas로 변환. 
# 추천점수 컬럼을 만듦
# (관객수*평점)/100

# 3. 추천점수가 높은순으로 출력


print(df)
print(df.sort_values('추천점수',ascending=False))


# # df.to_excel('daummovies.xlsx')

# df = pd.read_excel('daummovies.xlsx')

# print(df)