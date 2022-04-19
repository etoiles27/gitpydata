import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

rankall = soup.find("div",{"class":"col_inner"}) 

ranks = rankall.find_all("li")

for i, lis in enumerate(ranks):
    print("{:2d}위 : {}".format(i+1,lis.find("a",{"class":"title"}).get_text()))
    print("https://comic.naver.com"+lis.find("a",{"class":"title"})["href"])