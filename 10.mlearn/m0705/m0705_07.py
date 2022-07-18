from scipy import rand
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.special import expit,softmax
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

df_fish = pd.read_csv('https://bit.ly/fish_csv_data')

data = df_fish.drop(columns='Species').to_numpy()
label = df_fish['Species'].to_numpy()

train_data, test_data, train_label, test_label = train_test_split(data, label,random_state=42)

ss=StandardScaler()
train_scaled = ss.fit_transform(train_data)
test_scaled = ss.fit_transform(test_data)

classes = np.unique(train_label)

# 경사하강법 -> 알고리즘을 훈련
sc = SGDClassifier(loss='log_loss',max_iter=500, random_state=42,tol=None)
# sc = SGDClassifier(loss='log_loss', random_state=42)
# train_score=[]
# test_score=[]
# for idx in range(300):
#     sc.partial_fit(train_scaled,train_label, classes=classes)
#     train_score.append(sc.score(train_scaled, train_label))
#     test_score.append(sc.score(test_scaled, test_label))
# plt.plot(range(300),train_score, color='r')
# plt.plot(range(300),test_score)
# plt.show()

sc.fit(train_scaled,train_label)

sc.partial_fit(train_scaled,train_label)


score1 = sc.score(train_scaled,train_label)
score2 = sc.score(test_scaled,test_label)

print("train 정답률 :", score1)
print("test 정답률  :", score2)
