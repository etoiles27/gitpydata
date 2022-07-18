import numpy as np
import pandas as pd
# import os
# import gc
# import matplotlib.pyplot as plt
# import tensorflow as tf
from sklearn.model_selection import train_test_split
# from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# # 2 글자 이하 단어 삭제하는 함수
# def full_log_changer(sentence):
#     all_list_str = sentence.split() 
#     all_str = []
#     for list_str in all_list_str:
#         temp_w = []
#         for words in list_str:
#             if len(words)>2:
#                 temp_w.append(words)
        
#         joined_str = " ".join(temp_w)   
#         all_str.append(joined_str) 
#     return all_str
# train_df=pd.read_csv('10.mlearn/m0711/train.csv')
# test_df=pd.read_csv('10.mlearn/m0711/test.csv')
# # 특수문자, 숫자 제거
# train_df['full_log']=(train_df['full_log'].str.replace(r'[^a-zA-Zㄱ-ㅎ가-힣]', ' ', regex=True))
# test_df['full_log']=test_df['full_log'].str.replace(r'[^a-zA-Zㄱ-ㅎ가-힣]', ' ', regex=True)
# # 2글자 이하 단어 삭제 
# train_df['full_log']=full_log_changer(train_df['full_log'].str)
# test_df['full_log']=full_log_changer(test_df['full_log'].str)
# # 데이터 양이 방대하여 새로저장 
# train_df.to_csv('./trainModi.csv')
# test_df.to_csv('./testModi.csv')


# 1. 데이터 불러오기 
train_df=pd.read_csv('10.mlearn/m0711/trainModi3.csv')
test_df=pd.read_csv('10.mlearn/m0711/testModi3.csv')
submission_df=pd.read_csv('10.mlearn/m0711/sample_submission.csv')
 
    
train_log=list(train_df['full_log'])
train_level=np.array(train_df['level'])

# vectorizer=TfidfVectorizer(analyzer="word", max_features=10000)
# train_features=vectorizer.fit_transform(train_log)

# test_log=list(test_df['full_log'])
# test_features = vectorizer.transform(test_log)

CountVectorizer
vectorizer=CountVectorizer(analyzer="word", max_features=10000)
train_features=vectorizer.fit_transform(train_log)

test_log=list(test_df['full_log'])
test_features = vectorizer.transform(test_log)


train_data, test_data, train_label, test_label = train_test_split(train_features, train_level,stratify=train_level, random_state=42)


# 알고리즘 선택
rf=RandomForestClassifier(n_estimators=100)
# 학습 
rf.fit(train_data, train_label)

# 정확도 
score_test = rf.score(test_data, test_label)
score_train = rf.score(train_data, train_label)

print(score_train)
print(score_test)


pred=rf.predict(test_data)
crosstab = pd.crosstab(test_label, pred, rownames=['real'], colnames=['pred'])
print(crosstab)

preds=rf.predict(test_data)
probas=rf.predict_proba(test_data)
# preds[np.where(np.max(probas, axis=1) < 0.7)]=7
preds[np.where((np.max(probas, axis=1) < 0.6) & (preds == 3))]=7
preds[np.where((np.max(probas, axis=1) < 0.6) & (preds == 5))]=7
preds[np.where((np.max(probas, axis=1) < 0.7) & (preds == 1))]=7 
preds[np.where((np.max(probas, axis=1) < 0.7) & (preds == 0))]=7 

new_crosstab = pd.crosstab(test_label, preds, rownames=['real'], colnames=['pred'])
print(new_crosstab)



# results=rf.predict(test_features)
# results_proba=rf.predict_proba(test_features)
# results_new = results.copy()

# results_new[np.where((np.max(results_proba, axis=1) < 0.6))] = 7
# results_new[np.where((np.max(results_proba, axis=1)<0.8) & (results == 1))[0]]=7
# results_new[np.where((np.max(results_proba, axis=1)<0.8) & (results == 0))[0]]=7



# results_new[np.where((np.max(results_proba, axis=1) < 0.6) & (results == 3))]=7
# results_new[np.where((np.max(results_proba, axis=1) < 0.6) & (results == 5))]=7
# results_new[np.where((np.max(results_proba, axis=1) < 0.7) & (results == 1))]=7 
# results_new[np.where((np.max(results_proba, axis=1) < 0.7) & (results == 0))]=7 


# print(submission_df['level'].value_counts())


# submission_df['level'] = results_new
# submission_df.to_csv('sample_submission_v5.csv', index=False)