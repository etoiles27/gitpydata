from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from scipy.special import expit,softmax
from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


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


data = np.column_stack((data_length,data_weight))
label = np.concatenate((np.array(['도미']*len(bream_length)),np.array(['빙어']*len(smelt_length))))

train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)


# for i in range(1,20):
#     dt = DecisionTreeClassifier(max_depth=)
#     dt.fit(train_data,train_label)

dt = DecisionTreeClassifier()
dt.fit(train_data,train_label)
predict = dt.predict([[30,600]])
predict1 = dt.predict([[25,150]])
print(predict)
print(predict1)

score1 = dt.score(train_data, train_label)
score2 = dt.score(test_data, test_label)

print(score1)
print(score2)

plt.figure(figsize=(10,7))
plot_tree(dt,filled=True)
plt.show()







# tr = []
# te = []
# # 결정트리는 정규화가 필요없다
# for i in range(1,20):
#     dt = DecisionTreeClassifier(max_depth=i,random_state=42)
#     dt.fit(train_data, train_label)
#     tr.append(dt.score(train_data, train_label))
#     te.append(dt.score(test_data, test_label))

# plt.plot(tr)
# plt.plot(te)
# plt.show()


# dt = DecisionTreeClassifier(max_depth=5,random_state=42)
# dt.fit(train_data, train_label)
# score_tr = dt.score(train_data, train_label)
# score_te = dt.score(test_data, test_label)

# print(score_tr)
# print(score_te)

# plt.figure(figsize=(10,7))
# plot_tree(dt,filled=True,feature_names=['alcohol','sugar','pH'])
# plt.show()