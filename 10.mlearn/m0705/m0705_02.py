from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.special import expit
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
# 1. 데이터 전처리

length = bream_length + smelt_length
weight = bream_weight + smelt_weight

data = np.column_stack((length,weight))
label = np.concatenate((np.array(['도미']*len(bream_length)), np.array(['빙어']*len(smelt_length))))

train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)


ss = StandardScaler()
train_scaled = ss.fit_transform(train_data)
test_scaled = ss.fit_transform(test_data)
new_scaled1 = ss.fit_transform([[30,600]])
new_scaled2 = ss.fit_transform([[25,150]])

lr = LogisticRegression()
lr.fit(train_scaled,train_label)

result1 = lr.predict(new_scaled1)
result2 = lr.predict(new_scaled2)

result_proba = lr.predict_proba(test_scaled[:5])

score1 = lr.score(train_scaled, train_label)
score2 = lr.score(test_scaled, test_label)

print("30, 600 : ",result1)
print("25 150  : ",result2)

print(lr.coef_, lr.intercept_)

print(lr.predict(test_scaled))
print(result_proba)
print(score1)
print(score2)


plt.scatter(length, weight)
plt.scatter(30,600, color='r')
plt.scatter(25,150, color='y')

plt.show()










# df_fish = pd.read_csv('https://bit.ly/fish_csv_data')

# data = df_fish.drop(columns='Species').to_numpy()
# label = df_fish['Species'].to_numpy()

# train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

# idx = (train_label == 'Bream') | (train_label== 'Smelt')
# idx_te = (test_label == 'Bream') | (test_label== 'Smelt')

# train_bs = train_data[idx]
# test_bs = test_data[idx_te]
# train_bs_label = train_label[idx]
# test_bs_label = test_label[idx_te]

# ss = StandardScaler()
# train_scaled = ss.fit_transform(train_bs)
# test_scaled = ss.fit_transform(test_bs)



# lr = LogisticRegression()
# lr.fit(train_scaled,train_bs_label)

# result = lr.predict(test_scaled)
# result_proba = lr.predict_proba(test_scaled[:5])

# score1 = lr.score(train_scaled,train_bs_label)
# score2 = lr.score(test_scaled,test_bs_label)

# decision = lr.decision_function(test_scaled[:5])
# print(decision)
# print(result)
# print(result_proba)
# print('score1 : ', score1)
# print('score2 : ', score2)





