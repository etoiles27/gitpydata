import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글설정
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
# matplotlib.rcParams['font.family']='Apple Gothic'
matplotlib.rcParams['axes.unicode_minus']=False



# x=[1,2,3]
# y=[2,4,8]
# # 그래프생성
# plt.plot(x,y)
# # 상단 title 
# plt.title('실적그래프')
# # 라벨
# plt.xlabel('x축')
# plt.ylabel('y축')
# # 그래프 보여주기
# plt.show()


df = pd.read_excel('./score.xlsx')

x=df['이름']
y=df['국어']
z=df['영어']

plt.plot(x,y)
# plt.plot(x,z)

plt.xlabel('이름',loc='right')
plt.ylabel('국어점수',loc='top')

plt.show()