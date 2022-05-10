import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('score.xlsx')
x=df['이름']
y=df['키']

plt.figure(figsize=(10,5))
plt.bar(x,y,width=0.8,alpha=0.5)
plt.title('학생성적 그래프')
plt.xlabel('이름')
plt.ylabel('키')
for i,txt in enumerate(y):
    plt.text(x[i],y[i]+1,txt,ha='center')
    
# plt.yticks([170,180,190,200,210])
# y 축 그래프제한
# plt.xticks(rotation=45)
plt.ylim(160,210)
plt.show()