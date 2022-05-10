import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

df = pd.read_excel('score.xlsx')

x= np.arange(8) #df['이름']
y1=df['국어']
y2=df['영어']
y3=df['수학']


plt.figure(figsize=(8,5))
for i, txt in enumerate(y1):
    plt.text(i,y1[i],txt,ha='center')
    
    
plt.bar(x-0.25,y1,label='국어', width=0.25)
plt.bar(x,y2,label='영어',width=0.25)
plt.bar(x+0.25,y3,label='수학',width=0.25)
plt.ylim(0,110)
plt.xticks(x,df['이름'])
plt.legend()
plt.show()