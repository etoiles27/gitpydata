import pandas as pd
from random import *


def selweeks(num):
    wdate=''
    if num == '0':
        wdate = '월요일'
    elif num =='1':
        wdate = '화요일'
    elif num =='2':
        wdate = '수요일'
    elif num =='3':
        wdate = '목요일'
    elif num =='4':
        wdate = '금요일'
    elif num =='5':
        wdate = '토요일'
    elif num =='6':
        wdate = '일요일'
    
    return wdate
    
df = pd.read_excel('score.xlsx',index_col='지원번호')


rlist = [str(randint(0,6)) for i in range(len(df.index))]
# 기본 for문 
# for i in range(len(df.index)):
#     rlist.append(str(randint(0,6)))
# print(rlist)
    

    
df['요일'] = rlist
df['요일']=df['요일'].apply(selweeks)



# 이름    학교    키   국어   영어   수학  과학  사회 SW특기 요일
# 0        1      2    3      4      5    6     7   8       -1
cols = list(df.columns)
df = df[cols[0:3] + [cols[-1]] + cols[3:-1] ]




print(df)


# print(df)