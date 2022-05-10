import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


# 원그래프, 여러개 그래프, 눈금 2개로표시 
# color = ['#80cebe','#9fdebd','#7fd9d6','#ede868','#c4f2ce','#eff4e7']
color = ['#eadff2','#dccbed','#fee5e8','#fcb7d0','#f07bbb','#9979c1']
values = [30,25,20,13,10,2]
labels = ['python','java','javascript','c#','c++','etc']
plt.figure(figsize=(8,5))
explode = [0.05,0,0,0,0,0]
wedgeprops = {'width':0.6,'edgecolor':'w','linewidth':2}
def custom_autopct(pct):
    if pct>10:
        return'{:.1f}%'.format(pct)
    else:
        return ''
plt.pie(values,labels=labels,colors=color,pctdistance=0.7,wedgeprops=wedgeprops,explode=explode,autopct=custom_autopct,startangle=90,counterclock=False)
plt.title('원그래프')

plt.legend(loc=(1.1,0.3))
plt.show()