import pandas as pd 
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 1. 데이터 가져오기

# [ 도미 ]
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0,
33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0,
610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# [ 빙어 ]
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 2. 데이터 전처리
data_length = bream_length+smelt_length
data_weight = bream_weight+smelt_weight

data=[[l, w ] for l,w in zip(data_length,data_weight)]
label = ['도미']*len(bream_length)+['빙어']*len(smelt_length) 
train_data, test_data, train_label, test_label = train_test_split(data, label, test_size=0.3,stratify=label, random_state=42 )


# 2 - 2 numpy로 하기

data_np = np.column_stack((data_length,data_weight))
# ones,zeros array를 1개의 array로 변형
label_np = np.concatenate((np.ones(35),np.zeros(14)))
train_data_np, test_data_np, train_label_np, test_label_np = train_test_split(data_np, label_np, test_size=0.3,stratify=label, random_state=42 )


# 3. 알고리즘선택하기
clf = KNeighborsClassifier()
clf_np = KNeighborsClassifier()
# 4. 알고리즘 훈련
clf.fit(train_data,train_label)
clf_np.fit(train_data_np,train_label_np)
# 5. 예측
# result = clf.predict(test_data)
result = clf.predict([[30,160]])
result_np = clf_np.predict([[30,160]])
# 6. 정답률
score_testdata = clf.score(test_data, test_label)
score_traindata = clf.score(train_data, train_label)
score_testdata_np = clf_np.score(test_data_np, test_label_np)
score_traindata_np = clf_np.score(train_data_np, train_label_np)

print(result)
print(result_np)
print('test data score', score_testdata)
print('train data score', score_traindata)
print('test data score', score_testdata_np)
print('train data score', score_traindata_np)