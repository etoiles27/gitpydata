from gettext import npgettext
import sklearn
from sklearn.linear_model import SGDClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from tensorflow import keras

# train_data, test_data, train_label, test_label = train_test_split()

(train_data, train_label), (test_data, test_label) = keras.datasets.fashion_mnist.load_data()

# print(train_data.shape)
# print(test_data.shape)

print(train_label[:10])
fig, axs = plt.subplots(1,10,figsize=(10,10))
for i in range(10):
    axs[i].imshow(train_data[i], cmap='gray_r')
    axs[i].axis('off')

plt.show()
