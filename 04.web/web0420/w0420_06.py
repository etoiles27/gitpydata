from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.goodchoice.kr/product/result?keyword=%EC%98%A4%EC%85%98%EB%B7%B0"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

hotellist=[]
hoteljson={}





hotels = soup.find_all("li",{"class":re.compile("^list_4")})

# print(hotels[0])

hotelname11= hotels[0].find("div",{"class":"name"}).find_all("div",{"class":"badge"})
print(hotelname11)
hotelname22= hotels[4].find("div",{"class":"name"}).find_all("div",{"class":"badge"})
print(hotelname22)

for i, ho in enumerate(hotels):
    
    # print(title)
    hoteljson={}
    hotelname= ho.find("p",{"class":"pic"}).img["alt"]
    rate = float(ho.find("p",{"class":"score"}).em.get_text())
    rates = ho.find("p",{"class":"score"}).get_text()
    price_find = ho.find_all("b")
    price=0
    if len(price_find)>3:
        price = int(price_find[1].get_text()[:-1].replace(",",""))
    else:
        if price_find[0].get_text() =='판매 완료' or  price_find[0].get_text() =='다른날짜 확인':
            price=''
            continue
        price = int(price_find[0].get_text()[:-1].replace(",",""))
        
        
        
    
    
    n_s = rates.find('(')
    n_e = rates.find(')')
    rate_cnt = int(rates[n_s+1:n_e])
    
    hoteljson = {'name':hotelname,'rate':rate,"rateCnt":rate_cnt, "price":price}
    hotellist.append(hoteljson)
    
    
    # print(hotelname.strip())
    # print(rate)
    # print(rate_cnt)

print("총 호텔 수 : {}".format(len(hotellist)))
print("-"*30)
for i in range(len(hotellist)):
    if(hotellist[i]['rate']>=9.5) and hotellist[i]['rateCnt']>=500  :
        print("호텔이름 : {}".format(hotellist[i]['name']))
        print("호텔평점 : {}".format(hotellist[i]['rate']))
        print("호텔평   : {}".format(hotellist[i]['rateCnt']))
        print("호텔가격 : {}".format(hotellist[i]['price']))
        
        print("-"*30)