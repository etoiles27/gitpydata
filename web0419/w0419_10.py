import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")


tr = soup.find_all('tr')


avg = 0 
for i in range(1,len(tr)):
    star=tr[i].find("div",{"class":"rating_type"}).strong.get_text()
    avg += float(star)
    
    print(tr[i].img["src"])
    print(tr[i].find("td",{"class":"title"}).a.get_text())
    print(star)
    print(tr[i].find("td",{"class":"num"}).get_text())

print("평균평점: {}".format(avg/(len(tr)-1)) )


tbody =  soup.find_all('tbody')


