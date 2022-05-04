import requests
from bs4 import BeautifulSoup
import csv



url = "http://taas.koroad.or.kr/sta/acs/gus/selectTrnsportCnd.do?menuId=WEB_KMP_OVT_MVT_TAC_TAT"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")
caraccstats_rows = soup.find("tbody").find_all("tr")


filename ="교통사고비교.csv"
f=open(filename, 'w',encoding='utf-8-sig',newline='')
writer = csv.writer(f)


# print(caracciendts[0])
title = "년도	2016년	2017년	2018년	2019년	2020년"
title = title.split('\t')
writer.writerow(title)

mylist = []
print('-'*100)
print("{:20s} {:15s} {:15s} {:15s} {:15s} {:15s}".format('년도','2016년','2017년','2018년','2019년','2020년')  )
print('-'*100)
    
for stat in caraccstats_rows:
    columns = stat.find_all("td")
    mylist=[]
    for col in columns:
        mylist.append(col.get_text())
        print("{:15s}".format(col.get_text()),end='\t')
    print('')
    writer.writerow(mylist)
    


f.close()




