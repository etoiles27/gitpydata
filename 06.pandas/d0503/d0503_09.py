import pandas as pd
import numpy as np

def school(temp):
    result=''
    if temp == 1:
        result='구로고'
    elif temp == 2:
        result = '디지털고'
    elif temp == 3:
        result = '단지고'
    return result

def sw(temp):
    result=''
    if temp == 1:
        result='Java'
    elif temp == 2:
        result = 'c'
    elif temp == 3:
        result = 'Python'
    elif temp == 4:
        result = 'Javascript'
    elif temp == 5:
        result = np.nan
    return result


df = pd.read_excel('stu1000.xlsx',index_col='학번')


# 1 구로고 2 디지털고 3 단지고 
df['학교']=df['학교'].apply(school)

df['SW특기']=df['SW특기'].apply(sw)



result = df.groupby('학교')#['학년'].value_counts()

# print(result['학년'].value_counts())
# print(result['학년'].value_counts().loc['구로고'])

print(result['학년'].value_counts(normalize=True).loc['구로고'])