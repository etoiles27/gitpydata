import pandas as pd 
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 데이터 가져오기
df = pd.read_csv('10.mlearn/m0628/iris.csv', index_col='caseno')
# print(df.columns.values)

# 데이터 전처리 
data  = df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
label = df['Species']

train_data, test_data, train_label, test_label = train_test_split(data, label,test_size=0.2)


# 알고리즘 선택 knn
clf = KNeighborsClassifier()

# 알고리즘 실습
clf.fit(train_data,train_label)

# 예측
result = clf.predict(test_data)

# 정답률 
score1=clf.score(train_data,train_label)
score=clf.score(test_data,test_label)

# print('test data ', test_data)
# print('result ',result)
print('score ',score)
print('score ',score1)