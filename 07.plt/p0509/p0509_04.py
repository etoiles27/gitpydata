import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('score.xlsx')
x=df['지원번호']
y=df['키']

plt.plot(x,y,'bo-',label='국어')
plt.title('학생성적 그래프')
plt.xlabel('지원번호')
plt.ylabel('키')

# plt.text(x[0],y[0]+1,y[0],ha='center')
# plt.text(x[1],y[1],y[1],ha='center')

for i, txt in enumerate(y):
    plt.text(x[i],y[i],txt,ha='right')


plt.show()