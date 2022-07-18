import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from tensorflow import keras

# print(df.info())
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   label   20000 non-null  object
#  1   height  20000 non-null  int64
#  2   weight  20000 non-null  int64
# print(df.describe())
#              height        weight
# count  20000.000000  20000.000000
# mean     160.092050     57.377650
# std       23.385464     13.260121
# min      120.000000     35.000000
# 25%      140.000000     46.000000
# 50%      160.000000     57.000000
# 75%      180.000000     69.000000
# max      200.000000     80.000000

df = pd.read_csv('./11.deep/d0715/bmi.csv')
data = df.drop(columns='label')
# 원핫인코딩으로 변경 
one_encoding = pd.get_dummies(df['label'])
label = one_encoding.to_numpy()
print(label)
# print(label)

# 정규화 작업 
# ss = StandardScaler()
# data_scaled = ss.fit_transform(data)

data["weight"] /= 100
data["height"] /= 200
data = data.to_numpy()


# print(data_scaled)


train_data, test_data, train_label, test_label = train_test_split(data, label)

sub_data, val_data, sub_label, val_label = train_test_split(train_data, train_label)


# 4. 딥러닝 선언 
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(2,)))
model.add(keras.layers.Dense(512,activation='relu'))
model.add(keras.layers.Dense(256,activation='relu'))
model.add(keras.layers.Dropout(0.3))
model.add(keras.layers.Dense(3,activation='softmax'))
# 5. 딥러닝 훈련 
model.compile(optimizer="adam", loss='categorical_crossentropy', metrics='accuracy')

# 콜백 
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5')
early_stopping_cb =  keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)


# history = model.fit(train_data,train_label, epochs=20)
history = model.fit(sub_data,sub_label, epochs=30, validation_data=(val_data, val_label), callbacks=[checkpoint_cb, early_stopping_cb])

print(early_stopping_cb.stopped_epoch)



score = model.evaluate(test_data, test_label)
prd = model.predict([[141/200,64/100]])
print(prd)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['sub','val'])
plt.show()



m1 = [[0.91, 0.79]]
m2 = [[0.68,0.63]]
m3 = [[0.82,0.75]]

prd1 = model.predict(m1)
print(prd1)

prd2 = model.predict(m2)
print(prd2)
prd3 = model.predict(m3)
print(prd3)

print(model.predict([[161/200,68/100]]))
print(model.predict([[178/200,52/100]]))

# [[4.024756e-03 9.959752e-01 4.477730e-11]]

# [[9.9998546e-01 1.4517192e-05 1.9123944e-19]]

# [[9.9971884e-01 2.8116794e-04 1.4491202e-17]]
















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