
from lib2to3.pgen2.tokenize import tokenize
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from tensorflow import keras
from konlpy.tag import Okt
import urllib.request
from gensim.models import word2vec
from gensim.models import Word2Vec


urllib.request.urlretrieve('https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt', filename='ratings.txt')
train_data = pd.read_table('ratings.txt')
print(train_data.info())
print(train_data.describe())

train_data = train_data.dropna(how='any')
print(train_data.info())

# 한글 외 모든글자 삭제 
train_data['document'] = train_data['document'].str.replace("[^ㄱ-하-ㅣ가-힣]","",regex=True)
print(train_data.head())

okt = Okt()
# word2vec 형태소 분석 -> 글자안에 글자  
# 글자간의 벡터화를 해서 글자간의 관계를 형성
# [[]] 리스트 안 리스트 형태

tokenized_data = []
stopwords=['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

for sent in train_data['document']:
    temp_x = okt.morphs(sent, stem=True)
    temp_x = [word for word in temp_x if not word in stopwords]
    tokenized_data.append(temp_x)
    

# word2vec 
model = Word2Vec(sentences=tokenized_data,vector_size=100, window=5,min_count=5,workers=4, sg=0)

model.save('model_w2v.h5')
# model = word2vec.load('model_w2v.h5')

print(model.wv.most_similar("때"))