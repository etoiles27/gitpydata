import numpy as np
import pandas as pd
import re




sentence = '"Sep 24 10:02:22 localhost kibana: {""type"":""error"",""@timestamp"":""2020-09-24T01:02:22Z"",""tags"":[""warning"",""stats-collection""],""pid"":6458,""level"":""error"",""error"":{""message"":""No Living connections"",""name"":""Error"",""stack"":""Error: No Living connections\n    at sendReqWithConnection (/usr/share/kibana/node_modules/elasticsearch/src/lib/transport.js:226:15)\n    at next (/usr/share/kibana/node_modules/elasticsearch/src/lib/connection_pool.js:214:7)\n    at process._tickCallback (internal/process/next_tick.js:61:11)""},""message"":""No Living connections""}"'

print('원래문장')
print(sentence)
sentence = re.sub(r'[^a-zA-Zㄱ-ㅎ가-힣]', ' ', sentence)
print('숫자, 특수문자제거')
print(sentence)

list_str = sentence.split() 
print(sentence)

stri = []
for wd in list_str:
    if len(wd)>2:
        stri.append(wd)
joined_str = " ".join(stri)

print('2글자 이하단어, 공백 제거')
print(joined_str)


submission_df=pd.read_csv('sample_submission_v5.csv')
print(submission_df['level'].value_counts())


# 0    1000730
# 1     395708
# 3      12949
# 5       6493
# 7       2943
# 2         34
# 4         34
# 6         25