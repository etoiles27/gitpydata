
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글설정
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('./score.xlsx')


x=df['이름']
y=df['국어']
z=df['영어']


# plt.plot(x,y, label='성적',color='skyblue',linewidth=2, linestyle='--', marker='o',markerfacecolor='b',markersize=6)
# plt.plot(x,y,'bo:',label='성적',markerfacecolor='skyblue',markersize=6,markeredgecolor='navy')
plt.plot(x,y,'bo-.',lw=1,ms=6,mec='navy',mfc='skyblue',label='국어')
plt.plot(x,z,'ro-',lw=1,ms=6,mec='darkred',mfc='pink',label='영어')

# plt.bar(x,y,color='b',label='국어')
# plt.bar(x,z,color='r',label='영어',alpha=0.3)

plt.legend(loc=('upper right'))
plt.title('학생성적 그래프')
plt.xlabel('이름',loc='center')
plt.ylabel('국어점수',loc='center')



plt.show()