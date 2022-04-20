from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re

url = "https://browse.auction.co.kr/search?keyword=tv&itemno=&nickname=&encKeyword=tv&arraycategory=&frm=&dom=auction&isSuggestion=No&retry="
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

items = soup.find_all("div",{"class":"section--itemcard_info"})
itemlist =[]





for item in items:
    itemjson={}
    get_name = item.find("span",{"class":"text--title"})
    get_rate = item.find("div",{"class":"seller_awards"})
    get_rate_cnt =  item.find("span",{"class":"text--reviewcnt"})
    get_buy_cnt =  item.find("span",{"class":"text--buycnt"})
    if get_name:
        name = get_name.get_text()
    if get_rate:
        rate=float(get_rate["title"][5:-1])
    if get_rate_cnt:
        rate_cnt=int(get_rate_cnt.get_text()[3:].replace(",",""))
    if get_buy_cnt:
        buy_cnt=int(get_buy_cnt.get_text()[3:].replace(",",""))
    
    
    itemjason = {"name":name, "rate": rate, "rateCnt":rate_cnt, "buyCnt":buy_cnt}
    itemlist.append(itemjason)

# print(itemlist)
print("*"*20)

cnt = 0 
for i in range(len(itemlist)):
    if(itemlist[i]['rate']>=4.5) and itemlist[i]['rateCnt']>=1000 and itemlist[i]['buyCnt'] >=100 :
        
        cnt+=1
        print(cnt,".")
        print("제품명 : {}".format(itemlist[i]['name']))
        print("평점 : {}".format(itemlist[i]['rate']))
        print("후기수 : {}".format(itemlist[i]['rateCnt']))
        print("구매수 : {}".format(itemlist[i]['buyCnt']))



