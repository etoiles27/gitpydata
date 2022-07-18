
import numpy as np
import pandas as pd
from konlpy.tag import Okt

# konlpy 선언
okt = Okt()

f = open('./11.deep/d0715/book.txt', encoding='utf-8')
book = f.read()
# print(book)
lines = book.split('\n')


tokenized_data = []
stopwords=['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

for sent in lines['document']:
    temp_x = okt.morphs(sent, stem=True)
    temp_x = [word for word in temp_x if not word in stopwords]
    tokenized_data.append(temp_x)
    




# word2vec 

results = []

