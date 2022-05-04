
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글설정
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


df = pd.read_excel('movie.xlsx')


# print(df)
x=df['영화']
y=(df['관객 수']*0.01)
z=df['평점']


plt.plot(x,y,'bo-',lw=1,ms=6,mec='navy',mfc='skyblue',label='만명')
plt.plot(x,z,'ro-',lw=1,ms=6,mec='maroon',mfc='lightcoral',label='평점')


plt.legend(loc=('lower left'))
plt.title('영화 관객수 그래프')
plt.xlabel('영화 명',loc='center')
plt.ylabel('관객 수',loc='center')



plt.show()


df = pd.read_csv('test.csv', encoding='utf-8-sig')
df.to_excel('text.xlsx')