from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.special import expit,softmax
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

fish_df = pd.read_csv('https://bit.ly/fish_csv_data')
data = fish_df.drop(columns='Species').to_numpy()
label = fish_df['Species'].to_numpy()
# ['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt']
# print(fish_df.describe())
# print(fish_df.info())

train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

ss = StandardScaler()
train_scaled = ss.fit_transform(train_data)
test_scaled = ss.fit_transform(test_data)


train_score=[]
test_score=[]
classes = np.unique(train_label) # 7개
# sc.fit()  # reset 후에 다시 fit 
# sc.partial_fit() # fit을 update

# sc = SGDClassifier(loss='log_loss', random_state=42)
# for _ in range(500):
#     sc.partial_fit(train_scaled,train_label,classes=classes)
#     train_score.append(sc.score(train_scaled, train_label))
#     test_score.append(sc.score(test_scaled,test_label))


# plt.plot(train_score)
# plt.plot(test_score)
# plt.show()


sc = SGDClassifier(loss='log_loss', max_iter=100,tol=None,random_state=42)
sc.fit(train_scaled,train_label)

score1 = sc.score(train_scaled,train_label)
score2 = sc.score(test_scaled,test_label)

print(score1)
print(score2)

# sc.partial_fit(train_scaled,train_label)

# score3 = sc.score(train_scaled,train_label)
# score4 = sc.score(test_scaled,test_label)

# print(score3)
# print(score4)