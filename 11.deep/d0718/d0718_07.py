import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.model_selection import train_test_split 
from tensorflow import keras
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

matplotlib.rcParams['axes.unicode_minus']=False

(train_data, train_label),(test_data, test_label) = imdb.load_data(num_words=500)

# print(train_data.shape, test_data.shape)
# print(train_data[0])
# print(len(train_data[0]))
# print(train_label)
# print(np.unique(train_label))
# # 0 부정 1 긍정


# 데이터 전처리

sub_data, val_data, sub_label, val_label = train_test_split(train_data, train_label)

# print(sub_data.shape, val_data.shape)

# # train_data 문장 길이가 어떻게 되는지 확인 
# lengths = np.array([len(x) for x in train_data])

# print(np.mean(lengths), np.median(lengths))
# print(np.min(lengths), np.max(lengths))

# plt.hist(lengths)
# plt.show()

 # 100글자로 자르고 없는 부분을 0으로 채워준다 
train_seq = pad_sequences(sub_data, maxlen=100)
test_seq = pad_sequences(val_data, maxlen=100)
# print(len(sub_data[0]))
# print(len(sub_data[5]))
# print(len(sub_data[100]))
# print(len(train_seq[0]))
# print(len(train_seq[5]))
# print(len(train_seq[100]))
# print((train_seq[1]))

train_oh = keras.utils.to_categorical(train_seq)
test_oh = keras.utils.to_categorical(test_seq)



# 4. 딥러닝 선언 
model = keras.Sequential()
model.add(keras.layers.SimpleRNN(8, input_shape=(100,500)))
model.add(keras.layers.Dense(1,activation='sigmoid'))
model.summary()
# 5. 딥러닝 훈련 
rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics='accuracy')

# 콜백 
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-rnn.h5',save_best_only=True)
early_stopping_cb =  keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)


# history = model.fit(train_data,train_label, epochs=20)
history = model.fit(train_oh,sub_label, epochs=100, batch_size=64,validation_data=(test_oh, val_label), callbacks=[checkpoint_cb, early_stopping_cb])

print(early_stopping_cb.stopped_epoch)



score = model.evaluate(test_oh, val_label)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['sub','val'])
plt.show()


