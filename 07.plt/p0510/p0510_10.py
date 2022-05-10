
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

df1_m = pd.read_excel('1201인구현황.xlsx',skiprows=3,usecols='B:Y')
df1_w = pd.read_excel('1201인구현황.xlsx',skiprows=3,usecols='B,Z:AV')
df2_m = pd.read_excel('2201인구현황.xlsx',skiprows=3,usecols='B:Y')
df2_w = pd.read_excel('2201인구현황.xlsx',skiprows=3,usecols='B,Z:AV')

# 지역별 인구 현황 원그래프 
# print(df2_m)
# print(df1_w.columns)
print(df2_m['남 인구수'][1:])
# print(df1_m['행정기관'][1:])



labels = df1_m['행정기관'][1:]
values_m12 = df1_m['남 인구수'][1:].str.replace(',','').astype(int)
values_w12 = df1_w['여 인구수'][1:].str.replace(',','').astype(int)
values_m22 = df2_m['남 인구수'][1:].str.replace(',','').astype(int)
values_w22 = df2_w['여 인구수'][1:].str.replace(',','').astype(int)

labels_22 = df2_m['행정기관'][1:]


# plt.figure(figsize=(8,5))
# plt.pie(values_m12,labels=labels,autopct='%.1f%%')
# plt.title('2012 남자 인구 지역별')
# plt.show()

fig,axs = plt.subplots(2,2,figsize=(15,10))
axs[0,0].pie(values_m12,labels=labels,autopct='%.1f%%')
axs[0,0].set_title('2012 남자 지역별 인구')
axs[0,1].pie(values_w12,labels=labels,autopct='%.1f%%')
axs[0,1].set_title('2012 여자 지역별 인구')

axs[1,0].pie(values_m22,labels=labels_22,autopct='%.1f%%')
axs[1,0].set_title('2022 남자 지역별 인구')
axs[1,1].pie(values_w22,labels=labels_22,autopct='%.1f%%')
axs[1,1].set_title('2022 여자 지역별 인구')
plt.show()