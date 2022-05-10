import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

df = pd.read_excel('score.xlsx')

x=df['이름']
y1=df['국어']
y2=df['영어']
y3=df['수학']
plt.figure(figsize=(10,5))
# plt.bar(x,y1,color='r',label='국어')
# # plt.bar(x,y2,color='g')
# # plt.bar(x,y3,color='b')
# plt.bar(x,y2,bottom=y1,label='영어',color='g')
# plt.bar(x,y3,bottom=y1+y2,label='수학',color='b')
plt.barh(x,y1,color='r',label='국어')
plt.barh(x,y2,left=y1,label='영어',color='g')
plt.barh(x,y3,left=y1+y2,label='수학',color='b')
plt.xlim(0,350)

plt.grid(alpha=0.5,axis='y')
# plt.legend(ncol=3)
# plt.ylim(0,350)
plt.legend()
plt.show()