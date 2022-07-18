from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

perch_length = [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5, 44.0] 
perch_weight = [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0, 1000.0]
# numpy형태로 변경
perch_length = np.array(perch_length)
perch_weight = np.array(perch_weight)
# 배열크기 변경
perch_length = perch_length.reshape(-1,1)
perch_weight = perch_weight.reshape(-1,1)

# 1. 데이터 전처리
train_data, test_data, train_label, test_label = train_test_split(perch_length,perch_weight)

train_data = np.column_stack((train_data**2,train_data))
test_data = np.column_stack((test_data**2,test_data))



# 2. 알고리즘 선택
lr = LinearRegression()
# 3. 훈련
lr.fit(train_data,train_label)
# 4. 예측
result50 = lr.predict([[50**2,50]])
result100 = lr.predict([[100**2,100]])
predict_te = lr.predict(test_data)
# 5. 정확도
score_tr = lr.score(train_data,train_label)
score_te = lr.score(test_data,test_label)

# 오차범위 (실제값, 예측값의 오차)
mea = mean_absolute_error(test_label,predict_te)

point= np.arange(15,100)

print(result50)
print(result100)
print(score_tr)
print(score_te)
print(mea)

plt.scatter(perch_length, perch_weight)
plt.scatter(50, result50,color='r')
plt.scatter(100, result100,color='y')
# plt.plot([15,100],[15*lr.coef_+lr.intercept_, 100*lr.coef_+lr.intercept_ ], color='red')
plt.plot(point,lr.coef_[0]*point**2+lr.coef_[1]*point+lr.intercept_ )
plt.plot()
plt.xlabel("length")
plt.ylabel("weight")
plt.show()
