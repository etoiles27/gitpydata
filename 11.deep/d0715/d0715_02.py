import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from tensorflow import keras

(train_data, train_label), (test_data, test_label) = keras.datasets.fashion_mnist.load_data()

train_data = train_data/255.0
test_data = test_data/255.0

train_scaled, val_scaled, train_label, val_label = train_test_split(train_data, train_label)


# model = keras.Sequential()
# model.add(keras.layers.Flatten(input_shape=(28,28)))
# model.add(keras.layers.Dense(100, activation='relu'))
# model.add(keras.layers.Dropout(0.3))
# model.add(keras.layers.Dense(100, activation='softmax'))
# model.summary()
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')



# 모델 불러오기
model = keras.models.load_model('model_all.h5')
val_labs = np.argmax(model.predict(val_scaled),axis=-1)
val_re = model.predict(val_scaled)
score = model.evaluate(val_scaled, val_label)

print(score)
print(val_labs)
print((np.mean(val_labs==val_label)))