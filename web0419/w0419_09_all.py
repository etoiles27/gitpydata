import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

rankall = soup.find("div",{"class":"list_area daily_all"}) 



rankul = rankall.find_all("ul")


#print(rankul[0]) #mon
# aa = rankul[1].find_all("a",{"class":"title"})
# for i in aa:
#     print(i.get_text())

weeklist=["월요웹툰","화요웹툰","수요웹툰","목요웹툰","금요웹툰","토요웹툰","일요웹툰"]


for week in range(len(rankul)):
    rankd = rankul[week].find_all("a",{"class":"title"})
    print(weeklist[week])
    for i, cartoon in enumerate(rankd):
        print("{:2d}위 : {}".format(i+1,cartoon.get_text()))
        print("https://comic.naver.com"+cartoon["href"])

  