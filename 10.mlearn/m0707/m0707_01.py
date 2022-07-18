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


wine_df = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine_df.drop(columns='class').to_numpy()
label = wine_df['class'].to_numpy()
train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)


# cup core 개수 몇개 사용할지 정함 -1 core  
# 디폴트 10개 n_estimators=100
rf = RandomForestClassifier(random_state=42, n_jobs=-1)

scores = cross_validate(rf,train_data, train_label,return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']))
print(np.mean(scores['test_score']))

rf.fit(train_data,train_label)
score_te = rf.score(test_data,test_label)
print(score_te)
print(rf.feature_importances_)
