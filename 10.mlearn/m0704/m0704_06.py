import pandas as pd 
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('10.mlearn/m0628/iris.csv', index_col='caseno')
data = df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']].to_numpy()
label = df['Species'].to_numpy()

train_data, test_data, train_label, test_label = train_test_split(data,label)


clf = KNeighborsClassifier()
clf.fit(train_data, train_label)

result = clf.predict(test_data)
score = clf.score(test_data, test_label)

# [5.2, 3.4, 4.8, 0.2]

result_new = clf.predict([[5.2, 3.4, 4.8, 0.2]])
print(result_new)
print(score)