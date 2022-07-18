import pandas as pd 
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 데이터 가져오기
df = pd.read_csv('mushroom.csv')
# print(df.columns)


data = df[['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat']]



print(data.iloc[0][0])
for i in range(len(data)):
    for k in range(len(data.iloc[i])):
        data.iloc[i][k]= ord(data.iloc[i][k])


print(data)



label = df['poisonous']
# print(data)

# 방법2
# data = []
# label = []

# for row_index, rows in df.iterrows():
#     label.append(rows[0])
#     data.append
#     row_data = []
#     for v in rows[1:]:
#         row_data.append(ord(v))
#     data.append(row_data)

# print(data)
# print(label)

train_data, test_data, train_label, test_label = train_test_split(data, label, test_size=0.3,stratify=label, random_state=42 )

print(type(test_label))
# 알고리즘 선택 knn
clf = KNeighborsClassifier()

# 알고리즘 실습
clf.fit(train_data,train_label)

# 예측
result = clf.predict(test_data)

# 정답률 
score1=clf.score(train_data,train_label)
score=clf.score(test_data,test_label)

print('score ',score)
print('score ',score1)