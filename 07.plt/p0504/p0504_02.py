import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글설정
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
# matplotlib.rcParams['font.family']='Apple Gothic'
matplotlib.rcParams['axes.unicode_minus']=False


x=[1,2,3]
y=[-2,4,8]

plt.plot(x,y)
plt.show()



# df = pd.read_excel('./score.xlsx')

# print(df['지원번호'])
# print(df['국어'])

# x=df['이름']#[1,2,3]
# y=df['국어']#[2,4,8]
# z=df['영어']#[2,4,8]

# plt.plot(x,y)
# plt.plot(x,z)
# plt.show()