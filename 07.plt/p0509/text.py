import requests
from bs4 import BeautifulSoup

url = "https://www.musinsa.com/ranking/best?period=now&age=ALL&mainCategory=003&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=1&viewType=small&priceMin=&priceMax="
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

items = soup.findAll('li',{'class':'li_box'})

# title = items[0].find('p',{'class':'item_title'}).next_sibling
title = items[0].find_all('p',{'class':'item_title'})
print(len(title))
title1 = items[1].find_all('p',{'class':'item_title'})
print(len(title1))
print(title[1].get_text())

