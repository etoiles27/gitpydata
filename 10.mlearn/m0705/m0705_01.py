from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.special import expit
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt



df_fish = pd.read_csv('https://bit.ly/fish_csv_data')

data = df_fish.drop(columns='Species').to_numpy()
label = df_fish['Species'].to_numpy()

train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

idx = (train_label == 'Bream') | (train_label== 'Smelt')
idx_te = (test_label == 'Bream') | (test_label== 'Smelt')

train_bs = train_data[idx]
test_bs = test_data[idx_te]
train_bs_label = train_label[idx]
test_bs_label = test_label[idx_te]

ss = StandardScaler()
train_scaled = ss.fit_transform(train_bs)
test_scaled = ss.fit_transform(test_bs)



lr = LogisticRegression()
lr.fit(train_scaled,train_bs_label)

result = lr.predict(test_scaled)
result_proba = lr.predict_proba(test_scaled[:5])

score1 = lr.score(train_scaled,train_bs_label)
score2 = lr.score(test_scaled,test_bs_label)

decision = lr.decision_function(test_scaled[:5])
print(decision)
print(result)
print(result_proba)
print('score1 : ', score1)
print('score2 : ', score2)





