import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from tensorflow import keras



# 1. 데이터 불러오기
train_csv = pd.read_csv("10.mlearn/mnist/train.csv",header=None)
test_csv = pd.read_csv("10.mlearn/mnist/test.csv",header=None)

# 1000 * 785


train_data = np.array(list(train_csv.iloc[:,1:].values))
test_data = np.array(list(test_csv.iloc[:,1:].values))
train_label = train_csv[0].values
test_label = test_csv[0].values


print(np.unique(train_label,return_counts=True))


train_scaled = train_data/255.0
test_scaled = test_data/255.0




model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(784,)))
model.add(keras.layers.Dense(100,activation='relu'))
model.add(keras.layers.Dense(10,activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_label, epochs=5)

score1 = model.evaluate(train_scaled, train_label)
score2 = model.evaluate(test_scaled, test_label)

print(score1)
print(score2)

print(model.summary())