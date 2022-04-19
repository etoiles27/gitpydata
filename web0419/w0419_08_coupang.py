import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/categories/176522"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")


rankall = soup.find("ul",{"id":"productList"}) 
ranks = rankall.find_all("li")

for lis in ranks:
    print(lis.img["alt"])