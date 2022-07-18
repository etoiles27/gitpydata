
import numpy as np
import pandas as pd
from konlpy.tag import Okt

# konlpy 선언

f = open('./11.deep/d0715/book.txt', encoding='utf-8')
book = f.read()
# print(book)

okt = Okt()

{'날카로운':1,'분석':10}
word_dict={}
lines = book.split("\n")
for line in lines:
    # 명사인것만 
    malist = okt.pos(line, norm=True, stem=True)
    for taeso, pumsa in malist:
        if pumsa =='Noun':
            if not (taeso in word_dict):
                word_dict[taeso] = 0
            word_dict[taeso] += 1
            


keys = sorted(word_dict.items(),key=lambda x: x[1],reverse=True)
# print(sorted(word_dict.items(),key=lambda x: x[1],reverse=True))

for word, count in keys[:50]:
    print('{}:{}'.format(word,count),end='  ')
f.close()
