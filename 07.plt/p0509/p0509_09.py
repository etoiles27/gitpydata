import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


# stu 1000을 활용
# 합계점수가 높은 1학년 5명 
# 국어 영어 수학 과학 그래프를 출력


df = pd.read_excel('stu1000.xlsx',index_col='학번')
# print(df.columns)
df['합계'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']

filt = df['학년']==1
df1 = df.loc[filt].sort_values('합계',ascending=False)

df1_top5 = df1.iloc[0:5]


x = np.arange(5)
y1 = df1_top5['국어']
y2 = df1_top5['영어']
y3 = df1_top5['수학']
y4 = df1_top5['과학']

print(y1.iloc[0])
# plt.text(-0.4,y1[1],100,ha='center')

plt.figure(figsize=(10,5))
plt.bar(x-0.4,y1,label='국어', width=0.2)
plt.bar(x-0.2,y2,label='영어',width=0.2)
plt.bar(x,y3,label='수학',width=0.2)
plt.bar(x+0.2,y4,label='과학',width=0.2)

for i, txt in enumerate(y1):
    plt.text(x[i]-0.4,y1.iloc[i],txt,ha='center')
for i, txt in enumerate(y2):
    plt.text(x[i]-0.2,y2.iloc[i],txt,ha='center')
for i, txt in enumerate(y3):
    plt.text(x[i],y3.iloc[i],txt,ha='center')
for i, txt in enumerate(y4):
    plt.text(x[i]+0.2,y4.iloc[i],txt,ha='center')
plt.xticks(x,df1_top5['이름'])
# print(type(x))
# for x,y1,y2,y3,y4 in zip(x,y1,y2,y3,y4):
#     plt.text(x-0.4,y1+1,y1,ha='center')
#     plt.text(x-0.2,y2+1,y2,ha='center')
#     plt.text(x,y3+1,y3,ha='center')
#     plt.text(x-0.2,y4+1,y4,ha='center')

# print(type(x))
plt.legend(ncol=4)
plt.ylim(0,130)
plt.show()

