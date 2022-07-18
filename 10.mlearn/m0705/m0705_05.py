from scipy import rand
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.special import expit,softmax
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier




df = pd.read_csv('10.mlearn/m0705/iris.csv', index_col='caseno')

data = df.drop(columns='Species').to_numpy()
label = df['Species'].to_numpy()

train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

ss = StandardScaler()
train_scaled = ss.fit_transform(train_data)
test_scaled = ss.fit_transform(test_data)
new_scaled = ss.fit_transform([[5.1, 3.8, 1.8,0.5]])

# clist = [0.001,0.01,0.1,1,10,100,1000]
# trlist =[]
# telist=[]
# for cl in clist:
        
#     lr = LogisticRegression(C=cl)
#     lr.fit(train_scaled, train_label)
#     trlist.append(lr.score(train_scaled,train_label))
#     telist.append(lr.score(test_scaled,test_label))


# plt.plot(np.log10(clist),trlist, color='r')
# plt.plot(np.log10(clist),telist)
# plt.show()

lr = LogisticRegression(C=5)
lr.fit(train_scaled, train_label)

result = lr.predict(new_scaled)
result_proba = lr.predict_proba(test_scaled[:5])
print(result_proba)


decisions = lr.decision_function(test_scaled[:5])
print(decisions)
print(np.round(softmax(decisions,axis=1),decimals=3))

print(result)

score1 = lr.score(train_scaled,train_label)
score2 = lr.score(test_scaled,test_label)

print("train 정답률 :", score1)
print("test 정답률  :", score2)
