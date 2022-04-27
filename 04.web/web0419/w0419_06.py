import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

print("li class = rank01 : ", soup.find("li",{"class":"rank01"}))
print("text : ", soup.find("li",{"class":"rank01"}).get_text())

print("a 텍스트 글자: ", soup.find("li",{"class":"rank01"}).a.get_text())
aurl=soup.find("li",{"class":"rank01"}).a
atext=soup.find("li",{"class":"rank01"}).a.get_text()
print(atext)

print("1위 {}".format(atext))
print("바로가기 링크: ", "https://comic.naver.com"+aurl["href"])
