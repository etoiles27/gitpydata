
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus']=False

df1_m = pd.read_excel('1201인구현황.xlsx',skiprows=3,usecols='B:Y')
df1_w = pd.read_excel('1201인구현황.xlsx',skiprows=3,usecols='B,AB:AV')
df2_m = pd.read_excel('2201인구현황.xlsx',skiprows=3,usecols='B:Y')
df2_w = pd.read_excel('2201인구현황.xlsx',skiprows=3,usecols='B,AB:AV')

x_2012_m = (df1_m.iloc[0][3:].str.replace(',','').astype(int))/1000
x_2012_w = (df1_w.iloc[0][1:].str.replace(',','').astype(int))/1000

y=[]
for i, (rangename,cnt) in enumerate(x_2012_m.iteritems()):
    y.append(rangename)


x_2022_m = (df2_m.iloc[0][3:].str.replace(',','').astype(int))/1000
x_2022_w = (df2_w.iloc[0][1:].str.replace(',','').astype(int))/1000


fig,axs = plt.subplots(1,2,figsize=(15,8))
axs[0].barh(y,-x_2012_m,label='남자')
axs[0].barh(y,x_2012_w,label='여자')
axs[0].set_title('2012년도 전국 인구')
axs[0].legend()


axs[1].barh(y,-x_2022_m,label='남자')
axs[1].barh(y,x_2022_w,label='여자')
axs[1].set_title('2022년도 전국 인구')
axs[1].legend()

# axs[0,1].barh(y,x_2012_m)
# axs[0,0].barh(y,x_2012_w)


# plt.barh(y,-x_2012_m)
# plt.barh(y,x_2012_w)
# plt.barh(y,-x_2012_w)

# plt.barh(y,x_2022_m)
# plt.barh(y,-x_2022_w)


# plt.ylim([-2000, -1000, 0, 1000, 2000])
# fig, ax1 = plt.subplots()
# ax1.barh(y,-x_2012_m)
# ax2=ax1.twiny()
# ax2.barh(y,-x_2012_w)
plt.show()