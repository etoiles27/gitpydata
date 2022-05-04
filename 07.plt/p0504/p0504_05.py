from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글설정
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('./score.xlsx')

# print(df)
df['합계'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df['평균'] = (df['국어']+df['영어']+df['수학']+df['과학']+df['사회'])/5

x=df['이름']
y=df['합계']
z=df['평균']



plt.plot(x,y, label='성적',color='skyblue',marker='o',markerfacecolor='blue',markersize=6)
plt.bar(x,z)
plt.legend(loc=('upper right'))
plt.title('학생성적 그래프')
plt.xlabel('이름',color='black',loc='center')
plt.ylabel('점수',color='black',loc='top')

plt.yticks([0,100,200,300,400,500])

plt.show()