import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from tensorflow import keras

(train_data, train_label), (test_data, test_label) = keras.datasets.fashion_mnist.load_data()

train_scaled = train_data/255.0
test_scaled = test_data/255.0


model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

# 1
# model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics='accuracy')
# 2
# sgd = keras.optimizers.SGD(learning_rate=0.1)
# model.compile(optimizer=sgd, loss='sparse_categorical_crossentropy', metrics='accuracy')
# 3
# momentum = keras.optimizers.SGD(momentum=0.9, nesterov=True)
# model.compile(optimizer=momentum, loss='sparse_categorical_crossentropy', metrics='accuracy')

# 옵티마이져:  손실함수를 잘 찾아갈 수 있게 도와주는 알고리즘. 최적화 알고리즘.

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')




model.summary()
model.fit(train_scaled, train_label)

score = model.evaluate(test_scaled, test_label)