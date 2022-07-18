import pandas as pd 
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df_fish = pd.read_csv('https://bit.ly/fish_csv_data')

print(df_fish.columns)

data = df_fish.drop(columns='Species').to_numpy()
label = df_fish['Species'].to_numpy()

train_data, test_data, train_label, test_label = train_test_split(data, label,random_state=42)
ss = StandardScaler()
scaled_train = ss.fit_transform(train_data)
scaled_test = ss.fit_transform(test_data)
# new_scaled = ss.fit_transform([[105, 15.2, 19.5, 5.09, 3.42]])

# [105, 15.2, 19.5, 5.09, 3.42]

clf = KNeighborsClassifier()
clf.fit(scaled_train, train_label)


bream_smelt_idx = (train_label == 'Bream') | (train_label== 'Smelt')
bream_smelt_idx_te = (test_label == 'Bream') | (test_label== 'Smelt')

train_bream_smelt = scaled_train[bream_smelt_idx]
test_bream_smelt = scaled_test[bream_smelt_idx_te]
train_bream_smelt_label = train_label[bream_smelt_idx]
test_bream_smelt_label = test_label[bream_smelt_idx_te]

lr = LogisticRegression()
lr.fit(train_bream_smelt, train_bream_smelt_label)

result=clf.predict(test_bream_smelt)
score1 = clf.score(train_bream_smelt,train_bream_smelt_label)
score2 = clf.score(test_bream_smelt,test_bream_smelt_label)
print(result)
print(score1)
print(score2)



# result=clf.predict(new_scaled)

# proba = clf.predict_proba(new_scaled)
# print(np.round(proba,decimals=2))


# score1 = clf.score(scaled_train,train_label)
# score2 = clf.score(scaled_test,test_label)
# print(result)
# print(score1)
# print(score2)