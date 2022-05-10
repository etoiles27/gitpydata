import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

df = pd.read_excel('stu1000.xlsx')

# print(df.columns)
# print(df.groupby('학년').count())
# print(df['학년'].value_counts())


values = df['학년'].value_counts().sort_index()
# label = df['학년'].unique()

stu_cnt=[]
label = []

for i,(n,cnt) in enumerate(values.iteritems()):
   label.append(str(n)+'학년')
   stu_cnt.append(cnt)
   
print(label)
print(stu_cnt)



color = ['#eadff2','#dccbed','#fee5e8','#fcb7d0','#f07bbb','#9979c1']

plt.figure(figsize=(8,5))
# 거리띄우기
explode = [0.05,0,0,0,0]
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}



plt.pie(stu_cnt,labels=label,colors=color,wedgeprops=wedgeprops,pctdistance=0.7,autopct='%.1f%%',startangle=90,counterclock=False)

plt.title('학년 별 학생 비율')

plt.legend(loc=(1.1,0.3),title='학년')
plt.show()




