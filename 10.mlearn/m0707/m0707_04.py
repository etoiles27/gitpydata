from audioop import cross
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split, GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from scipy.special import expit,softmax
from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv('mushroom.csv')
data_df = df.drop(columns='poisonous')
label = df['poisonous'].to_numpy()
data = pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

for i in range(len(data_df)):
    for j in range(len(data_df.iloc[i])):
        data_df.replace(i, ord(data_df.iloc[i,j]))

print(data_df)
# new_data = []
# for i in range(len(data_df)):
#     row_data = []
#     for v in range(len(data_df.iloc[i])):
#         row_data.append(ord(data_df.iloc[i,v]))
#     new_data.append(row_data)
# data = new_data    


# train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

# rf = RandomForestClassifier(random_state=42, n_jobs=-1)

# scores = cross_validate(rf, train_data, train_label,n_jobs=-1, return_train_score=True)

# # print(scores)
# print(np.mean(scores['train_score']))
# print(np.mean(scores['test_score']))
# rf.fit(train_data, train_label)
# print(rf.feature_importances_)
# score_te = rf.score(test_data, test_label)
# print(score_te)




# print(data_df)
# print(label)






















# train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

# # 품종을 구별하는 알고리즘을 구현하시오
# # 랜덤포리스트 알고리즘 구현

# rf = RandomForestClassifier(random_state=42, n_jobs=-1)

# scores = cross_validate(rf, train_data, train_label,n_jobs=-1, return_train_score=True)

# # print(scores)
# print(np.mean(scores['train_score']))
# print(np.mean(scores['test_score']))
# rf.fit(train_data, train_label)
# print(rf.feature_importances_)
# score_te = rf.score(test_data, test_label)
# print(score_te)


