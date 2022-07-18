from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
from statistics import linear_regression


# linerregression 사용
# ㅇㅖ측하기. [30.4, 8.89, 4.22] 무게예측. 
# ridge model 사용 , alpha 값  사용

# 데이터 전처리 
df = pd.read_csv('./perch_full2.csv')
perch_weight = df['weight'].to_numpy()
perch_full = df[['length', ' height', ' width']].to_numpy()

train_data, test_data, train_label, test_label = train_test_split(perch_full,perch_weight, random_state=42)

# poly 
poly = PolynomialFeatures(degree=2, include_bias=False)
poly.fit(train_data)
train_poly = poly.transform(train_data)
test_poly = poly.transform(test_data)
new_poly = poly.transform([[30.4, 8.89, 4.22]])

# scale 
ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)
new_scaled = ss.transform(new_poly)

# linear regression 

lr = LinearRegression()
lr.fit(train_scaled, train_label)


# ridge 
ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled,train_label)

# lasso 
# alphalist = [0.01,0.01,0.1,1,10,100]
# train_score = []
# test_score=[]
# for list in alphalist:
#     lasso = Lasso(alpha=list)
#     lasso.fit(train_scaled,train_label)
#     train_score.append( lasso.score(train_scaled, train_label))
#     test_score.append(  lasso.score(test_scaled, test_label))

# plt.plot(np.log10(alphalist), train_score)
# plt.plot(np.log10(alphalist), test_score)
# plt.show()

lasso = Lasso(alpha=10)
lasso.fit(train_scaled,train_label)
score_la_tr = lasso.score(train_scaled, train_label)
score_la_te = lasso.score(test_scaled, test_label)
    
# score 

score_lr_tr = lr.score(train_scaled, train_label)
score_lr_te = lr.score(test_scaled, test_label)
predict_lr_te = lr.predict(test_poly)
predict_lr_new = lr.predict(new_poly)

score_rd_tr = ridge.score(train_scaled, train_label)
score_rd_te = ridge.score(test_scaled, test_label)
predict_rd_te = ridge.predict(test_poly)
predict_rd_new = ridge.predict(new_poly)


mea_lr = mean_absolute_error(test_label,predict_lr_te)
mea_rd = mean_absolute_error(test_label,predict_rd_te)



print()






# result = ridge.predict(new_poly)

# score_tr = ridge.score(train_poly, train_label)
# score_te = ridge.score(test_poly, test_label)

# predict_te = ridge.predict(test_poly)

# # 오차범위 (실제값, 예측값의 오차)
# mea = mean_absolute_error(test_label,predict_te)
# print(result)
# print(score_tr)
# print(score_te)
# print(mea)