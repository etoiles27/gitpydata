import pandas as pd 
import numpy as np
from sklearn import svm, metrics
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import glob, os.path,re


perch_length = [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 
20.0, 21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7, 
23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5, 27.5, 28.0, 
28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 
40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5, 44.0] 
perch_weight = [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 
85.0, 110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0, 
150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0, 218.0, 300.0, 
260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 
700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 
1000.0, 1100.0, 1000.0, 1000.0]

length = np.array(perch_length)
weight = np.array(perch_weight)


train_data, test_data, train_label, test_label = train_test_split(length,weight,test_size=0.2)

train_data=train_data.reshape(-1,1)
test_data=test_data.reshape(-1,1)

train_poly = np.column_stack((train_data**2, train_data))
test_poly = np.column_stack((test_data**2, test_data))


lr = LinearRegression()

lr.fit(train_poly,train_label)

result=lr.predict(test_poly)
score_train = lr.score(train_poly, train_label)
score = lr.score(test_poly, test_label)
print(score_train)
print(score)

print(lr.coef_)
print(lr.intercept_)



point = np.arange(15,101)
plt.scatter(length, weight)
result50=lr.predict([[50**2,50]])
result100=lr.predict([[100**2,100]])

print(result50)
print(result100)
plt.scatter(50, result50[0])
plt.scatter(100, result100[0])
plt.plot(point,lr.coef_[0]*point**2+lr.coef_[1]*point+lr.intercept_, color='red' )

plt.show()

