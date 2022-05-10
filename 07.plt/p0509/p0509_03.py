import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('score.xlsx')
x=df['지원번호']
y=df['국어']

plt.plot(x,y,'ro-',label='국어')
plt.title('학생성적 그래프')
plt.xlabel('지원번호')
plt.ylabel('국어성적')


# plt.text(x[0],y[0]+2)
for i, txt in enumerate(y):
    plt.text(x[i],y[i]+2,txt,ha='center')


plt.show()