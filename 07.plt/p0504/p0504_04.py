from cProfile import label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글설정
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


x = [1,2,3]
y = [192,194,198]

plt.plot(x,y, label='키높이')
# plt.legend(loc=(0.7,0.8))
plt.legend(loc=('upper right'))
plt.title('키높이 그래프')

plt.xlabel('번호',color='blue',loc='center')
plt.ylabel('키',color='red',loc='top')


plt.xticks([1,2,3])

plt.show()