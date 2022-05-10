
from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False


data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2016, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], 
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}

df= pd.DataFrame(data)
df.sort_values('개봉 연도',inplace=True)
df = df.reset_index()
plt.figure(figsize=(10,5))
# print(df)
# x = list(df['개봉 연도'])
# y = list(df['평점'])
x = (df['개봉 연도'])
y = (df['평점'])

print(x)
# 
# print(y)
for i, txt in enumerate(y):
    print(x[i],':   ', txt)

    if (i%2 == 1):
        plt.text(x[i],y[i]+0.2,txt,ha='center')
    else:
        plt.text(x[i],y[i]-0.2,txt,ha='center')
    
plt.plot(x,y,'ro-',label='영화평점')
plt.title('인기 영화 개봉 연도 별 평점 그래프')
plt.xlabel('개봉 연도')
plt.ylabel('평점')
plt.xticks([2005,2010,2015,2020])
plt.ylim(7,10)
plt.legend()
plt.show()