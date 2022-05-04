import pandas as pd

# 함수
def changeSchoolname(num):
    school = ''
    if num == 1:
        school='구로고'
    elif num == 2:
        school='디지털고'
    elif num == 3:
        school='단지고'
    return school
def changeSW(num):
    sw = ''
    if num == 1:
        sw='Java'
    elif num == 2:
        sw='c'
    elif num == 3:
        sw='Python'
    elif num == 4:
        sw='Javascript'
    elif num == 5:
        sw='JAVA'
    return sw
    
def setScore(num):
    result = ''
    if num >= 90:
        result='A'
    elif num >= 80:
        result='B'
    elif num >= 70:
        result='C'
    elif num >= 60:
        result='D'
    else:
        result='F'
    return result


# 1번 학교 컬럼변경, 1-구로고 2-디지털고 3 단지고 
# sw특기, 1-JAVA 2- c 3 - Python 4 Javascript 5 JAVA
df = pd.read_excel('stu1000.xlsx')

df['학교']=df['학교'].apply(changeSchoolname)
df['SW특기']=df['SW특기'].apply(changeSW)


# 2번 합계, 평균, 평가 컬럼 추가
df['합계'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['평균'] = (df['국어']+df['영어']+df['수학']+df['과학']+df['사회'])/5

df['평가'] = df['평균'].apply(setScore)



# 3번 합계점수가 400점이상인 학생의 수학평균을 구하시요 

filt = df['합계']>400
mathmean_oversum400=df.loc[filt,'수학'].mean()
print(mathmean_oversum400)
# print(df.loc[filt,'수학'].mean())
# print(df[filt].describe())

