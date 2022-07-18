import pandas as pd 
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import glob, os.path,re



def makeData(url):
    files = glob.glob(url)
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
            count = list(map(lambda n:n/total, count))
            data.append(count)
            label.append(lang)
    return data, label 

train_url = '10.mlearn/m0630/train/*.txt'
train_data , train_label = makeData(train_url)


test_url = '10.mlearn/m0630/test/*.txt'
test_data , test_label = makeData(test_url)


t1_url = '10.mlearn/m0630/en-100.txt'
t1_data , t2_label = makeData(t1_url)
t2_url = '10.mlearn/m0630/fr-100.txt'
t2_data , t2_label = makeData(t2_url)


# clf = KNeighborsClassifier()
clf = svm.SVC()
clf.fit(train_data,train_label)

result = clf.predict(test_data)
result1 = clf.predict(t1_data)
result2 = clf.predict(t2_data)
score = clf.score(test_data, test_label)

print(result)
print(score)
print(result1)
print(result2)