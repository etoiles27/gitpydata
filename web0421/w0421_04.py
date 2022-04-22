from types import coroutine
import requests
from bs4 import BeautifulSoup
import re
import csv



url = "https://finance.naver.com/sise/sise_market_sum.naver?&page={}".format(1)
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")
musics = soup.find_all("tr",{"class":"list"})

filename = "시가총액1-200.csv"
f=open(filename,'w',encoding="utf-8-sig",newline='')
writer = csv.writer(f)

data_rows=soup.find("table",{"class":"type_2"}).tbody.find_all("tr")


# 상단 제목 넣기 
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE"
# csv 파일은 list type 만 가능 
title = title.split('\t')
writer.writerow(title)

collist=[]
list=[]
# print(len(data_rows))
for row in data_rows:
    columns = row.find_all("td")
    collist=[]
    if len(columns)<2:
        continue
    for col in columns:
        coltxt = col.get_text().strip()
        # coltxt= re.sub(r'[%,+-]','',coltxt)
        collist.append(coltxt)
    writer.writerow(collist)
    list.append(collist)    

f.close()


    
    