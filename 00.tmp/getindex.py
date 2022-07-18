import requests
from bs4 import BeautifulSoup

url="https://www.collectluxe.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")


a = soup.prettify()
print(a)

with open('aaa.html','w', encoding='utf-8') as file:
    file.write(res.text)