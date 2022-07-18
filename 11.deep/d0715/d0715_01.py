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

