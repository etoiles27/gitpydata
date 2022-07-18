
import numpy as np
import pandas as pd
from konlpy.tag import Okt
from bs4 import BeautifulSoup
import codecs
# konlpy 선언

fp = codecs.open('./11.deep/d0715/BEXX0003.txt', 'r',encoding='utf-16')
soup = BeautifulSoup(fp,'html.parser')
body = soup.find("body").find("text").get_text()

# 1글자 제외, 명사만 출력. 

lines = body.split("\n")
# print(len(lines))
okt = Okt()

word_dict =[]

for line in lines:
    malist = okt.pos(line, norm=True, stem=True)
    r = []
    for taeso, pumsa in malist:
        if (pumsa == 'Noun') & (len(taeso)>1):
            
            if not (taeso in word_dict):
                word_dict[taeso] = 0
            word_dict[taeso] += 1


keys = sorted(word_dict.items(),key=lambda x: x[1],reverse=True)
for word, count in keys[:50]:
    print('{}:{}'.format(word,count),end='  ')