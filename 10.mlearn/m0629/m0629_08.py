from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 1. 데이터 불러오기
train_csv = pd.read_csv("10.mlearn/mnist/train.csv",header=None)
test_csv = pd.read_csv("10.mlearn/mnist/test.csv",header=None)


# # 2. 데이터 전처리
# # 이미지 데이터 일 경우 0-1까지의 수로 표시
# # map함수
def func(a):
    output=[]
    for i in a:
        output.append(float(i)/256)
    return output 

train_data = list(map(func, train_csv.iloc[:,1:].values))  # 0-255:256
test_data = list(map(func,test_csv.iloc[:,1:].values))
train_label = train_csv[0].values
test_label = test_csv[0].values



# # 3. 알고리즘 선택
clf = KNeighborsClassifier()

# # 4. 실습훈련
clf.fit(train_data,train_label)

# # 5. 예측
result = clf.predict(test_data)
print("결과값 : ",result)

# # 6. 정답률
score1 = clf.score(train_data,train_label)
score2 = clf.score(test_data,test_label)
print("정답률 1 : ",score1)
print("정답률 2 : ",score2)