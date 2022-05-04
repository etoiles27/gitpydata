import pandas as pd


# DataFrame Join
# concat 행기준으로 - 각각의 DataFrame 합침
# df = pd.concat([data1,data2,data3])

# 2차원데이터
data ={
    '이름':['주바다','공유진','송선유','양홍욱'],
    '키':[180,182,188,179],
    '몸무게':[47,49,50,45]
}

data2={
    '이름':['주바다','공유진','송선유','윤상운'],
    '전공':['컴퓨터공학','매카닉공학','독일어학','컴퓨터공학'],
    '실력':['고급','중고급','특급','중고급']
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

### DataFrame join하는 방법 
### merge - 열기준(이름)으로 합침 
# inner - data,data2 같은 데이터가 있는 경우만 합침
# df = 주바다,공유진,송선유,양홍욱
# df2 = 주바다,공유진,송선유,윤상운
mdf = pd.merge(left=df,right=df2, how='inner',on='이름')
print(mdf)

# left=df 기준으로 합침
mdf2 = pd.merge(left=df,right=df2, how='left',on='이름')
# mdf2['전공'][3]='자율전공'
# mdf2['실력'][3]='초급'
print(mdf2)

# right=df2 기준으로 합침
mdf3 = pd.merge(left=df,right=df2,how='right',on='이름')
print(mdf3)

# df,df2의 모든 열 합침
mdf4 = pd.merge(left=df,right=df2,how='outer',on='이름')
print(mdf4)

