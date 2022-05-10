# score 5명   국어성적을 원그래프로출력 

from pickle import TRUE
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

df = pd.read_excel('score.xlsx')

df2 = df[:5].sort_values('국어', ascending=False)

# print(df2)
stu_name =df2['이름'][:5] 
kor_score=df2['국어'][:5]
color = ['#eadff2','#dccbed','#fee5e8','#fcb7d0','#f07bbb','#9979c1']

plt.figure(figsize=(8,5))
# 거리띄우기
explode = [0.05,0,0,0,0]
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}
def custom_autopct(pct):
    if pct>10:
        return'{:.1f}%'.format(pct)
    else:
        return '생략'


plt.pie(kor_score,labels=stu_name,colors=color,wedgeprops=wedgeprops,pctdistance=0.7,autopct=custom_autopct,startangle=90,counterclock=False)

plt.title('학생성적')

plt.legend(loc=(1.1,0.3))
plt.show()