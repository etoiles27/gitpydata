from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('score.xlsx')

# x=[1,2,3]
# y=[-2,-4,8]
x=df['지원번호']
y=df['키']
plt.plot(x,y,'ro--',label='키')
plt.title('학생그래프')
plt.xlabel('학생번호',color='r')
plt.xlabel('키',color='b')
plt.grid(axis='x')

plt.show()