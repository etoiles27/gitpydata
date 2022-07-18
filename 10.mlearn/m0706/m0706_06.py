from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import train_test_split
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
sub_data, value_data, sub_label, value_label = train_test_split(train_data, train_label)

# tr = []
# te = []
# # 결정트리는 정규화가 필요없다
# for i in range(1,20):
#     dt = DecisionTreeClassifier(max_depth=i,random_state=42)
#     dt.fit(train_data, train_label)
#     tr.append(dt.score(train_data, train_label))
#     te.append(dt.score(test_data, test_label))

# plt.plot(tr)
# plt.plot(te)
# plt.show()


# dt = DecisionTreeClassifier(max_depth=5,random_state=42)
dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_data, train_label)
score_tr = dt.score(train_data, train_label)
score_te = dt.score(test_data, test_label)
score_sb = dt.score(sub_data, sub_label)
score_va = dt.score(value_data, value_label)

print(score_tr)
print(score_te)
print(score_sb)
print(score_va)

# plt.figure(figsize=(10,7))
# plot_tree(dt,filled=True,feature_names=['alcohol','sugar','pH'])
# plt.show()



