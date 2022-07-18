from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
from statistics import linear_regression
df = pd.read_csv('10.mlearn/m0630/perch_full.csv')
perch_full = df.to_numpy()
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0, 1000.0])

perch_full = df.to_numpy()
train_data, test_data, train_label, test_label = train_test_split(perch_full,perch_weight, random_state=42)

poly = PolynomialFeatures(degree=5, include_bias=False)
poly.fit(train_data)
train_poly = poly.transform(train_data)
test_poly = poly.transform(test_data)
new_poly = poly.transform([[30.4, 8.89, 4.22]])

ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)
new_scaled = ss.transform(new_poly)

# lr = LinearRegression()
# lr.fit(train_poly,train_label)


# 알파값 찾기 ----------------------------------------------------
# alphalist = [0.01,0.01,0.1,1,10,100]
# train_score = []
# test_score=[]
# for list in alphalist:
#     ridge = Ridge(alpha=list)
#     ridge.fit(train_scaled,train_label)
#     train_score.append( ridge.score(train_scaled, train_label))
#     test_score.append(  ridge.score(test_scaled, test_label))

# plt.plot(np.log10(alphalist), train_score)
# plt.plot(np.log10(alphalist), test_score)
# plt.show()
# 알파값 찾기 ----------------------------------------------------


ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled,train_label)

result = ridge.predict(new_poly)

score_tr = ridge.score(train_poly, train_label)
score_te = ridge.score(test_poly, test_label)

predict_te = ridge.predict(test_poly)

# 오차범위 (실제값, 예측값의 오차)
mea = mean_absolute_error(test_label,predict_te)
print(result)
print(score_tr)
print(score_te)
print(mea)