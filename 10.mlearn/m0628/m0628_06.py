import pandas as pd 
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


# [ 도미 ]
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0,
33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0,
610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# [ 빙어 ]
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
# 1. 데이터 전처리

# 데이터 합치기 
length = bream_length+smelt_length
weight = bream_weight+smelt_weight
# 데이터의 길이
totallen = len(length)
# print(totallen)
# 라벨만들기 
label = np.concatenate((np.ones(35),np.zeros(14)))
# ['도미']*len(bream_length)+['빙어']*14
# print(label)
#  데이터 묶기
data=[[l, w ] for l,w in zip(length,weight)]
# print(data)






mean = np.mean(data,axis=0)
std = np.std(data, axis=0)
train_scaled = (data-mean)/std

print(train_scaled)




# train_data,test_data,train_label,test_label = train_test_split(data,label, test_size=0.3, stratify=label, random_state=44)
train_data = data
train_label= label

# test = [[30,600]]
test = [[25,150]]
# # test_label=[]

print(train_data)
# print(test_data)


length = 30 # float(input('길이를 입력하세요 : '))
weight = 600 # float(input('무게를 입력하세요 : '))
# # 알고리즘 선택
clf = KNeighborsClassifier()
# # 데이터학습훈련
clf.fit(train_data, train_label)
distances, indexs = clf.kneighbors([[25,150]])

# # 데이터예측
result = clf.predict(test)

print(result)
# # 정답률
# score=clf.score(test_data,test_label)
# plt.scatter(bream_length, bream_weight, c='skyblue')
# plt.scatter(smelt_length, smelt_weight, c='blue')
# plt.scatter(smelt_length, smelt_weight, c='blue')
# plt.scatter(30, 600, marker='*',c='red')
# plt.scatter(25, 150, marker='x',c='red')

# plt.show()
# # print(score)
new = ([25,150] -mean)/std

ss=StandardScaler()




plt.scatter(train_scaled[:,0], train_scaled[:,1], c='skyblue')
plt.scatter(train_scaled[indexs,0], train_scaled[indexs,1], c='blue')
plt.scatter(new[0],new[1] ,marker='x',c='red')
plt.show()