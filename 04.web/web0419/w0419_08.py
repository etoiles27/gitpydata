import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")


rankall = soup.find("ol",{"id":"realTimeRankFavorite"}) 
cartoons = rankall.find_all("li")

#print(cartoons[0])

# for i in range (len(cartoons)):
#     print(cartoons[i].a.get_text())

for i, cartoon in enumerate(cartoons):
    print("{:2d}위 : {}".format(i+1,cartoon.a.get_text()))
    print("https://comic.naver.com"+cartoon.a["href"])

# rank1 = soup.find("li",{"class":"rank01"})
# print(rank1.find_next_sibling("li").find("a").get_text())
# print(rank1.next_sibling.next_sibling)