import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


# 원그래프, 여러개 그래프, 눈금 2개로표시 
color = ['#80cebe','#9fdebd','#7fd9d6','#ede868','#c4f2ce','#eff4e7']
values = [30,25,20,13,10,2]
labels = ['python','java','javascript','c#','c++','etc']
plt.figure(figsize=(8,5))
explode = [0.1,0,0,0,0,0]
plt.pie(values,labels=labels,colors=color,explode=explode,autopct='%.1f%%',startangle=90,counterclock=False)
plt.title('원그래프')

plt.legend(loc=(1.1,0.3))
plt.show()