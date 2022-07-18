from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from tensorflow import keras
from konlpy.tag import Okt

# konlpy 선언
okt = Okt()

# pos 형태소 분석, norm 그래욬ㅋㅋ -> 그래요 , stem 그래요-> 그렇다
malist = okt.pos('아버지 가방에 들어가신다', norm=True, stem=True)

print(malist)



























# (train_data, train_label), (test_data, test_label) = keras.datasets.fashion_mnist.load_data()

# train_data = train_data/255.0
# test_data = test_data/255.0

# train_scaled, val_scaled, train_label, val_label = train_test_split(train_data, train_label)

# model = keras.Sequential()
# model.add(keras.layers.Flatten(input_shape=(28,28)))
# model.add(keras.layers.Dense(100, activation='relu'))
# model.add(keras.layers.Dense(10, activation='softmax'))

# model.summary()
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# history = model.fit(train_scaled, train_label, epochs=20, validation_data=(val_scaled, val_label))

























# train_scaled, val_scaled, train_label, val_label = train_test_split(train_data, train_label)


# model = keras.Sequential()
# model.add(keras.layers.Flatten(input_shape=(28,28)))
# model.add(keras.layers.Dense(100, activation='relu'))
# model.add(keras.layers.Dropout(0.3))
# model.add(keras.layers.Dense(100, activation='softmax'))
# model.summary()
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')


# # callback
# # epochs 20번 가장 손실률 낮은 시점찾아 model 저장
# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5')
# early_stopping_cb =  keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)
# history = model.fit(train_scaled, train_label, epochs=20, validation_data=(val_scaled, val_label),callbacks=[checkpoint_cb,early_stopping_cb])


# print(early_stopping_cb.stopped_epoch)
# score = model.evaluate(val_scaled, val_label)

# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.legend(['sub','val'])
# plt.show()