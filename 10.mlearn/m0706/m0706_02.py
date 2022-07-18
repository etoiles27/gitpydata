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


lr = LogisticRegression(C=1)
lr.fit(train_scaled, train_label)

score_tr = lr.score(train_scaled, train_label)
score_te = lr.score(test_scaled, test_label)

print(score_tr)
print(score_te)