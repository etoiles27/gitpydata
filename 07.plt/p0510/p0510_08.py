
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('score.xlsx')
x=df['이름']
y=df['키']
z=df['국어']


# plt.plot(x,y)
# plt.plot(x,z)


fig, ax1 = plt.subplots()
ax1.set_ylim(160,210)
ax1.plot(x,y,'o-')
ax2=ax1.twinx()
ax2.plot(x,z,'rv-')
ax2.set_ylim(0,110)
ax2.set_ylabel('국어')
ax1.set_ylabel('키')
ax1.set_xlabel('이름')

for i, val in enumerate(z):
    ax2.text(i,val+2,val,ha='center')
    
    
for i, val in enumerate(y):
    if (i == 0) | (i ==2) :
        ax1.text(i,val-5,val,ha='center')
    else:
        ax1.text(i,val+2,val,ha='center')


plt.show()