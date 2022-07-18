from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from scipy.special import expit,softmax
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

wine_df = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine_df.drop(columns='class').to_numpy()
label = wine_df['class'].to_numpy()


train_data, test_data, train_label, test_label = train_test_split(data, label, random_state=42)
ss = StandardScaler()
train_scaled = ss.fit_transform(train_data)
test_scaled = ss.fit_transform(test_data)

train_score=[]
test_score=[]
classes = np.unique(train_label) 

sc = SGDClassifier(loss='log_loss', random_state=42)
for _ in range(500):
    sc.partial_fit(train_scaled,train_label,classes=classes)
    train_score.append(sc.score(train_scaled, train_label))
    test_score.append(sc.score(test_scaled,test_label))


plt.plot(train_score)
plt.plot(test_score)
plt.show()

