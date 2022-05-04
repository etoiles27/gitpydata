from numpy import inner
import pandas as pd

member_info ={
    '이름':['주바다','공유진','송선유','양홍욱'],
    '성별':['여','여','여','남'],
    '전화번호':['010-1111-1111','010-1111-2222','010-1111-3333','010-1111-4444']
}

member_score={
    '이름':['공유진','주바다','윤상운','송선유'],
    '국어':[100,99,95,100],
    '영어':[95,99,99,100]
}

df1 = pd.DataFrame(member_info)
df2 = pd.DataFrame(member_score)



#  5-1 같은것만 join
mi_df = pd.merge(left=df1, right=df2, how='inner',on='이름')

print(mi_df)

#  5-2 모두존재 join
mo_df = pd.merge(left=df1, right=df2, how='outer',on='이름')

print(mo_df)