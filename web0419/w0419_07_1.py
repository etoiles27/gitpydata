import requests
from bs4 import BeautifulSoup

url = "https://news.daum.net/"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"class":"cont_thumb"}))


aurl=soup.find("a",{"class":"link_txt"})
atext=soup.find("a",{"class":"link_txt"}).get_text()

print(atext.strip())
print(aurl["href"])