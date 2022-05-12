import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

df = pd.read_excel('score.xlsx')
print(df)


# x = df['국어']
# y = df['영어']

# s_size = np.random.rand(len(x))*1000
# # print(s_size)
# # print(x)
# # print(y)

# plt.scatter(x,y,s=s_size)
# plt.show()



x = df['이름']
y= np.random.randint(60,101,len(x))

for i, txt in enumerate(y):
    plt.text(x[i],txt+2,txt,ha='center')
plt.bar(x,y)
plt.ylim(50,110)
plt.show()