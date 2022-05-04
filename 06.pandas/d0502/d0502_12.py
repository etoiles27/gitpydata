from re import A
import pandas as pd


def calRate(score):
    tmp = float(score)

    if tmp >=90:
        score = 'A'
    elif tmp>=80:
        score = 'B'    
    elif tmp>=70:
        score = 'C'
    elif tmp>=60:
        score = 'D'
    else:
        score='F'
        
    return score
    
df = pd.read_excel('score.xlsx',index_col='지원번호')

df['사회점수평가']=df['사회'].astype(str)

df['사회점수평가']=df['사회점수평가'].apply(calRate)



# 이름    학교    키   국어   영어   수학  과학  사회 SW특기 사회점수평가
# 0        1      2    3      4      5    6     7   8       -1
cols = list(df.columns)
df = df[cols[0:8] + [cols[-1]] + [cols[-2]] ]


df['합계'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['평균'] = df['합계']/5

df['평균평가']=df['평균'].astype(str)
df['평균평가']=df['평균평가'].apply(calRate)

print(df)





