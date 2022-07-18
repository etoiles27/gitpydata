from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('10.mlearn/m0630/perch_full.csv')
perch_full = df.to_numpy()
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0, 1000.0])


# df['weight']=perch_weight
# df.to_csv('perch_full2.csv')
# df = pd.read_csv('./perch_full2.csv')
# print(df)

perch_full = df.to_numpy()
train_data, test_data, train_label, test_label = train_test_split(perch_full,perch_weight)

# lr = LinearRegression()
# lr.fit(train_data,train_label)
# print(lr.coef_, lr.intercept_)

poly = PolynomialFeatures(degree=2)
poly.fit(train_data)
train_poly = poly.transform(train_data)
test_poly = poly.transform(test_data)

lr = LinearRegression()
lr.fit(train_poly,train_label)