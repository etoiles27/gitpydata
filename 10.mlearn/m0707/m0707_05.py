
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import SGDClassifier, LogisticRegression,LinearRegression
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split, GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from scipy.special import expit,softmax
from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


# 투수 - 2018 연봉예측 알고리즘


df = pd.read_csv('C:/pydata/10.mlearn/m0707/picher_stats_2017.csv')

one_encoding=pd.get_dummies(df['팀명'])

df = df.join(one_encoding)
print(df)
pi_data = df.drop(columns=['연봉(2018)','선수명','팀명']).to_numpy()
pi_label = df['연봉(2018)'].to_numpy()

# 데이터 전처리
train_data, test_data, train_label, test_label = train_test_split(pi_data, pi_label, random_state=42)

ss = StandardScaler()
train_scaled = ss.fit_transform(train_data)
test_scaled = ss.fit_transform(test_data)




rf = RandomForestRegressor(random_state=42, n_jobs=-1)

scores = cross_validate(rf, train_data, train_label,n_jobs=-1, return_train_score=True)

# print(scores)
print(np.mean(scores['train_score']))
print(np.mean(scores['test_score']))
rf.fit(train_data, train_label)
print(rf.feature_importances_)
score_te = rf.score(test_data, test_label)
print(score_te)







# 알고리즘선택




# sc = SGDClassifier(loss='log_loss', max_iter=100, random_state=42)
# sc.fit(train_scaled,train_label) 
# print(sc.score(train_scaled,train_label))
# print(sc.score(test_scaled,test_label))

# # 1. linear regression 
# lr = LinearRegression()
# lr.fit(train_data, train_label)
# score_tr = lr.score(train_data, train_label)
# score_te = lr.score(test_data, test_label)
# print(score_tr)
# print(score_te)

# #  2. logistric Regression
# lr = LogisticRegression()
# lr.fit(train_scaled, train_label)
# score_tr = lr.score(train_scaled, train_label)
# score_te = lr.score(test_scaled, test_label)
# print(score_tr)
# print(score_te)



# print(pi_data)
# print(pi_label)






# 팀 가중치 - 2017 순위 - 기아, 두산, 롯데, NC, SK, LG, 넥센, 한화, 삼성, KT
#                        10    9      8    7   6   5   4     3    2    1
# print(data['팀명'][0])

# for i in range(len(data['팀명'])):
#     if data['팀명'][i] == 'KIA':
#         data['팀명'][i] = 10
#     elif data['팀명'][i] == '두산':
#         data['팀명'][i] = 9
#     elif data['팀명'][i] == '롯데':
#         data['팀명'][i] = 8
#     elif data['팀명'][i] == 'NC':
#         data['팀명'][i] = 7
#     elif data['팀명'][i] == 'SK':
#         data['팀명'][i] = 6
#     elif data['팀명'][i] == 'LG':
#         data['팀명'][i] = 5
#     elif data['팀명'][i] == '넥센':
#         data['팀명'][i] = 4
#     elif data['팀명'][i] == '한화':
#         data['팀명'][i] = 3
#     elif data['팀명'][i] == '삼성':
#         data['팀명'][i] = 2
#     elif data['팀명'][i] == 'KT':
#         data['팀명'][i] = 1
#     else:
#         data['팀명'][i] = 0
        


# print(data)
# print(label)


# # train and test split 
# train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

# # algorithm choose 
# lr = LogisticRegression()
# # rf = RandomForestRegressor(random_state=42)

# # train 
# lr.fit(train_data, train_label)

# # predict 

# # score
# score1 = lr.score(train_data,train_label)
# score2 = lr.score(test_data,test_label)
# print(score1)
# print(score2)