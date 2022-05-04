
import pandas as pd

url = 'https://race.kra.co.kr/dbdata/fileDownLoad.do?fn=internet/seoul/horse/20220501sdb1.txt&meet=1'

df = pd.read_csv(url, encoding='euc-kr')

df.to_csv('test.csv',encoding='utf-8-sig')