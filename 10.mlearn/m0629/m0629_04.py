from cProfile import label
from http.client import ImproperConnectionState
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


df = pd.read_csv('mushroom.csv')

data =  df[['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat']]
label = df['poisonous']

new_data = []
for i in range(len(data)):
    row_data = []
    for v in range(len(data.iloc[i])):
        row_data.append(ord(data.iloc[i,v]))
    new_data.append(row_data)
data = new_data    
train_data, test_data, train_label, test_label = train_test_split(data, label)

# 알고리즘 선택 knn
# clf = KNeighborsClassifier()
clf = svm.SVC()

# 알고리즘 실습
clf.fit(train_data,train_label)

# 예측
result = clf.predict(test_data)

# 정답률 
score1=clf.score(train_data,train_label)
score=clf.score(test_data,test_label)

print('score ',score)
print('score ',score1)
