from cProfile import label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


# 산점도 그래프

df = pd.read_excel('score.xlsx')

df['학년']=[3,3,2,1,1,3,2,2]


x= df['영어']
y= df['수학']


size=[3000,3000,2000,1000,1000,3000,2000,2000]
# size=np.random.rand(8)*1000
# print(df)

plt.figure(figsize=(7,5))
plt.scatter(x,y,s=size,c=df['학년'],cmap='magma')

plt.colorbar(ticks=[1,2,3],label='학년',shrink=0.5,orientation='horizontal')



plt.title('영어-수학 상관관계')
plt.xlabel('영어 성적')
plt.ylabel('수학 성적')
# plt.legend()
plt.show()
