import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers) # url 파일정보 가져오기
res.raise_for_status()  # 200코드 확인

# with open("aaa.html","w",encoding="utf-8") as f:
#     f.write(res.text)

# text를 lxml, css 파싱, beautifulsoup에서 html파싱해서soup 가져옴
soup = BeautifulSoup(res.text,"lxml")
# print(soup)

# print("title : ", soup.title)
# print("title  제목 : ", soup.title.get_text())

# print("a : ", soup.a)
# print("a 텍스트 글자: ", soup.a.get_text())
# print("a attr : ", soup.a.attrs)
# print("a href: ", soup.a["href"])

# print("div : ", soup.div)
# print("div attr : ", soup.div.attrs)
# print("div id : ", soup.div["id"])

print("div id=menu :  " , soup.find("div",attrs={"id":"menu"}))