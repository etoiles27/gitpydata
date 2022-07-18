import pandas as pd
import numpy as np
from sklearn import svm, metrics
import sklearn
from sklearn.model_selection import train_test_split

def nameChange(species):
    if species == 'setosa':
        return 0
    elif species == 'versicolor':
        return 1
    else:
        return 0 
    
df = pd.read_csv('10.mlearn/m0628/iris.csv', index_col='caseno')
# print(df.columns)
# print(df['Species'].unique())

# 데이터 전처리 'SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth' 120개 분리, species 120개 분리 
# 데이터를 랜덤하게 분리할 필요가 있어보임. .. 순서대로하면 특정품종이 트레인되지 않음

# df_shuffled=sklearn.utils.shuffle(df)
df_shuffled =  df.sample(frac=1) 



train_data = df_shuffled[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']][0:120]
train_label=df_shuffled['Species'][0:120]

test_data=df_shuffled[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']][120:]
test_label=df_shuffled['Species'][120:]

print(train_label)
print(test_label)

# 알고리즘 선택
clf = svm.SVC()

# 데이터학습훈련
clf.fit(train_data, train_label)
# 데이터예측
result = clf.predict(test_data)
# 정답률
score=clf.score(test_data,test_label)


print(result)
print(score)

