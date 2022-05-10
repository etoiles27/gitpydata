from cProfile import label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('score.xlsx')
x=df['지원번호']
y=df['국어']

plt.figure(figsize=(10,5),dpi=72,facecolor='g') # 그래프 크기조절  72dip(웹) 200dpi(인쇄용)
plt.plot(x,y,label='국어')
plt.plot(x,df['영어'],label='영어')
plt.plot(x,df['수학'],label='수학')
plt.title('학생성적 그래프')
plt.xlabel('학생번호')
plt.ylabel('국어성적')
plt.yticks([0,20,40,60,80,100,120])
plt.legend(loc='upper right')



plt.savefig('학생성적.png')
plt.show()