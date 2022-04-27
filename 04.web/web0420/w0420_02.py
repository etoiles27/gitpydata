import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=703846&weekday=tue"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")


cartoons = soup.find_all("td",{"class":"title"})

for i , cartoon in enumerate(cartoons):
    web_title=cartoon.a.get_text()
    web_link="https://comic.naver.com"+cartoon.a["href"]
   
    print(web_title, end="\t")
    print(web_link)