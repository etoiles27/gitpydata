import pandas as pd 
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import glob, os.path,re

files = glob.glob('10.mlearn/m0630/train/*.txt')
# print(files)

data = [] # a-z 26 개
label = [] # 4개 en, fr, id, tl

for file_name in files:
    basename = os.path.basename(file_name)
    lang =basename.split('-')[0]
    with open(file_name,'r',encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        code_a = ord('a')
        code_z = ord('z')
        count = [0]*26
        
        for ch in text:
            code_current = ord(ch)
            if code_a<=code_current<=code_z:
                count[code_current-code_a] += 1
            total = sum(count)
            count = list(map(lambda n: n/total, count))
            data.append(count)
            label.append(lang)



test_files = glob.glob('10.mlearn/m0630/test/*.txt')
# print(files)

test_data = [] # a-z 26 개
test_label = [] # 4개 en, fr, id, tl

for file_name in test_files:
    basename = os.path.basename(file_name)
    lang =basename.split('-')[0]
    with open(file_name,'r',encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        code_a = ord('a')
        code_z = ord('z')
        count = [0]*26
        
        for ch in text:
            code_current = ord(ch)
            if code_a<=code_current<=code_z:
                count[code_current-code_a] += 1
            total = sum(count)
            count = list(map(lambda n: n/total, count))
            test_data.append(count)
            test_label.append(lang)