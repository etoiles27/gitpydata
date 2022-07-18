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


# 2 글자 이하 단어는 의미 없다 판단되어 삭제 
def full_log_changer(sentence):
    all_list_str = sentence.split() 
    all_str = []
    for list_str in all_list_str:
        temp_w = []
        for words in list_str:
            if len(words)>2:
                temp_w.append(words)
        
        joined_str = " ".join(temp_w)   
        all_str.append(joined_str) 
    return all_str
   


# 1. 데이터 불러오기 
train_df=pd.read_csv('10.mlearn/m0711/train.csv')
test_df=pd.read_csv('10.mlearn/m0711/test.csv')

# 2 글자 이하 단어는 의미 없다 판단되어 삭제 
def full_log_changer(sentence):
    all_list_str = sentence.split() 
    all_str = []
    for list_str in all_list_str:
        temp_w = []
        for words in list_str:
            if len(words)>3:
                temp_w.append(words)
        
        joined_str = " ".join(temp_w)   
        all_str.append(joined_str) 
    return all_str


train_df['full_log']=(train_df['full_log'].str.replace(r'[^a-zA-Zㄱ-ㅎ가-힣]', ' ', regex=True))
test_df['full_log']=test_df['full_log'].str.replace(r'[^a-zA-Zㄱ-ㅎ가-힣]', ' ', regex=True)



train_df['full_log']=full_log_changer(train_df['full_log'].str)
test_df['full_log']=full_log_changer(test_df['full_log'].str)


train_df.to_csv('./trainModi3.csv')
test_df.to_csv('./testModi3.csv')
