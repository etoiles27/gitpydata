
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('score.xlsx')

x=df['이름']
y=df['국어']
z=df['영어']
k=df['수학']
w=df['사회']

fig,axs = plt.subplots(2,2,figsize=(15,8))
axs[0,0].bar(x,y,label='국어')
axs[0,0].set_xlabel('이름')
axs[0,0].set_ylabel('국어')
axs[0,0].legend()
axs[0,0].grid(linestyle='--',linewidth=0.5)
axs[0,0].set_facecolor('#ffeeff')
axs[0,0].set_title('국어 막대 그래프')
axs[0,1].plot(x,z,label='영어')
axs[0,1].plot(x,k,label='수학')
axs[0,1].legend(loc='upper center')
# axs[1,0].scatter(z,k)
# axs[1,0].set_xlabel('영어')
# axs[1,0].set_ylabel('수학')
axs[1,0].barh(x,w,alpha=0.5)
axs[1,1].pie(k,labels=x)

plt.show()