from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

df = pd.read_excel('score.xlsx')
x=df['이름']
y=df['키']

# plt.bar(x,y,width=0.5)
# plt.ylim(165,210)
bar = plt.barh(x,y)
plt.xlim(165,210)
bar[0].set_hatch('/')
bar[1].set_hatch('//')
bar[2].set_hatch('x')
bar[3].set_hatch('xx')
bar[4].set_hatch('.')
bar[5].set_hatch('..')


plt.grid(alpha=0.5,axis='y')
plt.legend(ncol=3)
plt.ylim(0,350)
plt.show()