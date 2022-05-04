import requests
from bs4 import BeautifulSoup

# url = "https://shoppinghow.kakao.com/siso/p/hotdeal/list/"
url = 'https://www.coupang.com/'
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

print(soup.prettify())

listsall = soup.find('div',{'id':'personalizedGW'})
print(listsall)

# bests=soup.find("div",{"id":"bestRankProductList"})


# print(soup)

# print(res.text)


# with open("aaa.html","w",encoding="utf-8") as f:
#     f.write(res.text)