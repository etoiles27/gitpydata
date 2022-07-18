from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split, GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from scipy.special import expit,softmax
from sklearn.tree import DecisionTreeClassifier, plot_tree

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


wine_df = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine_df.drop(columns='class').to_numpy()
label = wine_df['class'].to_numpy()


train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)

# 결정트리로 그리드서치사용 
# prams 3 개를 사용
# 최종 스코어를 구하세요 

params = {'min_impurity_decrease':np.arange(0.0001,0.001,0.0001),
          'max_depth':range(5,20,1),
          'min_samples_split':range(2,100,10)}

# ['ccp_alpha', 'class_weight', 'criterion', 'max_depth', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_samples_leaf', 'min_samples_split', 'min_weight_fraction_leaf', 'random_state', 'splitter']


gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)
gs.fit(train_data, train_label)

dt = gs.best_estimator_

score1 = dt.score(test_data,test_label)
score2 = dt.score(train_data,train_label)

print(score2)
print(score1)

print(gs.best_params_)
print(gs.best_score_)






















# params = {'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005]}
# gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)
# # 5 번 반복 훈련
# gs.fit(train_data, train_label)
# # 우수한 fit을 dt에. 
# dt = gs.best_estimator_

# # score = cross_validate(dt, train_data, train_label)
# score = dt.score(train_data, train_label)
 
# print(score)
# # print(gs.best_estimator_)
# print(gs.best_params_)
# print('-'*20)
# print(gs.cv_results_)

