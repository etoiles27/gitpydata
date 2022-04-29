import pandas as pd

import matplotlib.pyplot as plt 



# dic type 
data = {
'이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
'학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
'키' : [197, 184, 168, 187, 188, 202, 188, 190],
'국어' : [90, 40, 80, 40, 15, 80, 55, 100],
'영어' : [85, 35, 75, 60, 20, 100, 65, 85],
'수학' : [100, 50, 70, 70, 10, 95, 45, 90],
'과학' : [95, 55, 80, 75, 35, 85, 40, 95],
'사회' : [85, 25, 75, 80, 10, 80, 35, 95],
'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}


# x = data['이름']
# y=data['국어']

# plt.plot(x,y)
# plt.title('Korean')
# plt.show()

df = pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df.index.name='번호'
# print(df.index)

df.reset_index(inplace=True)
#df.reset_index(drop=True,inplace=True)

df.set_index('이름',inplace=True)

df.sort_index(ascending=False,inplace=True)





print(df)