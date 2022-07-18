from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.special import expit,softmax
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt



df_fish = pd.read_csv('https://bit.ly/fish_csv_data')
data = df_fish.drop(columns='Species').to_numpy()
label = df_fish['Species'].to_numpy()

train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

ss = StandardScaler()
train_scaled = ss.fit_transform(train_data)
test_scaled = ss.fit_transform(test_data)

# clist = [0.001,0.01,0.1,1,10,100]
# tr_sc = []
# te_sc = []
# for cin in clist:
#     lr = LogisticRegression(C=cin) # c가 낮으면 규제가 강함, 
#     lr.fit(train_scaled, train_label)
#     tr_sc.append(lr.score(train_scaled,train_label))
#     te_sc.append(lr.score(test_scaled,test_label))
    
# plt.plot(np.log10(clist), tr_sc, color='r')
# plt.plot(np.log10(clist), te_sc, color = 'b')
# plt.show()

    
lr = LogisticRegression(C=10) # c가 낮으면 규제가 강함, 
lr.fit(train_scaled, train_label)

result = lr.predict(test_scaled)
result_proba = lr.predict_proba(test_scaled[:5])

score1 = lr.score(train_scaled,train_label)
score2 = lr.score(test_scaled,test_label)

print(result)
print(result_proba)
print(score1)
print(score2)


# z, 시그모이드 => 이진분류
decisions = lr.decision_function(test_scaled[:5])
print(decisions)
print(expit(decisions))

# 소프트맥스 => 다중분류
# print(np.round(softmax(decisions),decimals=4))
print(decisions)
print(np.round(softmax(decisions,axis=1),decimals=3))