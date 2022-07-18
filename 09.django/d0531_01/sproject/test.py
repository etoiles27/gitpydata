import requests
from bs4 import BeautifulSoup
import re

myheaders={"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

url="http://www.nalthin.com/cal/e.html"
res=requests.get(url,headers=myheaders)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

print(soup.prettify())

with open('data2.txt','w',encoding='utf-8') as f:
    f.write(res.text)