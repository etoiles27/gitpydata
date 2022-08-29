import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from tensorflow import keras
import matplotlib
import urllib.request
matplotlib.rcParams['axes.unicode_minus']=False




(train_data, train_label), (test_data, test_label) = keras.datasets.fashion_mnist.load_data()

train_scaled = train_data.reshape(-1,28,28,1)/255.0
test_scaled =  test_data.reshape(-1,28,28,1)/255.0


print(train_data.info())