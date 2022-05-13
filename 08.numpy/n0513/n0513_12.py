import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States', 'Netherlands', 'Germany', 'Switzerland', 'Belarus', 'Austria', 'France', 'Poland', 'China', 'Korea','Sweden', 'Czech Republic', 'Slovenia', 'Japan','Finland', 'Great Britain', 'Ukraine', 'Slovakia','Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]


# 각 국가별 획득한 메달 포인트의 합을 구하시오.
# DataFrame을 출력하시오
# 금 : 4 은: 2 동: 1

# gold_arr = np.array(gold)
# silver_arr = np.array(silver)
# bronze_arr=np.array(bronze)

# total = gold_arr*4+silver_arr*2+bronze_arr

# print(total)

# x = countries
# y = total
# plt.bar(x,y)
# plt.xticks(rotation=270)
# plt.show()



df1 = pd.DataFrame({
    
    'countries' : ['Russian Fed.', 'Norway', 'Canada', 'United States', 'Netherlands', 'Germany', 'Switzerland', 'Belarus', 'Austria', 'France', 'Poland', 'China', 'Korea','Sweden', 'Czech Republic', 'Slovenia', 'Japan','Finland', 'Great Britain', 'Ukraine', 'Slovakia','Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan'],

})
df2 = pd.DataFrame({'gold' : [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
'silver' : [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0],
'bronze' : [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

})


md_mx = np.array(df2)
arr00=np.array([4,2,1])
pt_mx = np.dot(md_mx,arr00)


df=pd.concat([df1,df2],axis=1)
df['points'] = pt_mx
print(df)

# df['countries']=df1
# df['gold']=df2['gold']
# df['silver']=df2['silver']
# df['bronze']=df2['bronze']
# df['points'] = pt_mx

# print(df)
# df.to_excel('medal.xlsx')
# x = df['countries']
# y = df['points']
# plt.bar(x,y)
# plt.xticks(rotation=270)
# plt.show()


dfA = pd.DataFrame({
    
    'countries' : ['Russian Fed.', 'Norway', 'Canada', 'United States', 'Netherlands', 'Germany', 'Switzerland', 'Belarus', 'Austria', 'France', 'Poland', 'China', 'Korea','Sweden', 'Czech Republic', 'Slovenia', 'Japan','Finland', 'Great Britain', 'Ukraine', 'Slovakia','Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan'],
'gold' : np.array([13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]),
'silver' :np.array( [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]),
'bronze' :np.array( [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1])

})

mm = df[['gold','silver','bronze']]
print(mm)

# list1 = []
# for i in range(len(df['gold'])):
#     list2 = [df['gold'][i],df['silver'][i],df['bronze'][i]]
#     list1.append(list2)
#     list2=[]
    
    
# arr_medal = np.array([df['gold'],df['silver'],df['bronze']])
# arr_pt = [4,2,1]
# arr_points = np.dot(list1, arr_pt)
# print(arr_points)
# # df['point'] = df['gold']*4+df['silver']*2+df['bronze']
# df['points'] = arr_points
# print(df)


# x = df['countries']
# y = df['points']
# plt.bar(x,y)
# plt.xticks(rotation=270)
# plt.show()
