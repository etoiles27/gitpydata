import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")


btext = soup.find("a",{"id":"recommand_titleName_0"}).get_text()
burl = soup.find("a",{"id":"recommand_titleName_0"})

print("1위 {}".format(btext))
print("바로가기 링크: ", "https://comic.naver.com"+burl["href"])



aurl=soup.find("div",{"class":"rc_info"}).a
atext=soup.find("div",{"class":"rc_info"}).a.get_text()


print("1위 {}".format(atext))
print("바로가기 링크: ", "https://comic.naver.com"+aurl["href"])
