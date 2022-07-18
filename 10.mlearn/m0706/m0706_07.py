from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
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


dt = DecisionTreeClassifier()
score = cross_validate(dt, train_data, train_label)

print(np.mean(score['test_score']))


dt.fit(train_data,train_label)
print(dt.score(test_data,test_label))

# 'fit_time': array([0.        , 0.01562214, 0.        , 0.        , 0.01574206]), 
# 'score_time': array([0.        , 0.        , 0.        , 0.        , 0.00101566]), 
# 'test_score': array([0.85948718, 0.85641026, 0.8798768 , 0.85112936, 0.84907598])}

