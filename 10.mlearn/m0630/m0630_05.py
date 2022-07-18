
import pandas as pd 
import numpy as np
from sklearn import svm, metrics
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import glob, os.path,re


perch_length = [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 
20.0, 21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7, 
23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5, 27.5, 28.0, 
28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 
40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5, 44.0] 
perch_weight = [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 
85.0, 110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0, 
150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0, 218.0, 300.0, 
260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 
700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 
1000.0, 1100.0, 1000.0, 1000.0]

length = np.array(perch_length)
weight = np.array(perch_weight)


train_data, test_data, train_label, test_label = train_test_split(length,weight)
# print(train_data)
train_data=train_data.reshape(-1,1) # -1은 모든 데이터를 가져와서 1행으로 바꾸겟다
test_data=test_data.reshape(-1,1) # -1은 모든 데이터를 가져와서 1행으로 바꾸겟다
# print(train_data)
knr = KNeighborsRegressor(n_neighbors = 5)
# knn이웃하는 5개의 데이터를 추출
# ne = knr.kneighbors([[18.5]])
# print(ne)
knr.fit(train_data,train_label)
result = knr.predict(test_data)

print(result)

score = knr.score(test_data,test_label)
score1 = knr.score(train_data,train_label)

print(score)
print(score1)

mae = mean_absolute_error(test_label,result)

print(mae)
s = knr.predict([[18.5]])
distances, indexs = knr.kneighbors([[18.5]])
print(s)
plt.scatter(length, weight)
plt.scatter(18.5,s[0])
plt.scatter(train_data[indexs], train_label[indexs], color='r')

plt.xlabel("length")
plt.ylabel("weight")
plt.show()

