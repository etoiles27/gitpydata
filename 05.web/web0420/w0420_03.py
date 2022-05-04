import requests
from bs4 import BeautifulSoup

url = "http://corners.gmarket.co.kr/Bestsellers"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")


t1_div=soup.find("div",{"id":"topPlusItems"})
t2_div= t1_div.find_next_sibling("div")
items=t2_div.find_all("li")

#print(items[0])
for i in range(200):
    print(items[i].img["alt"])
    print(items[i].strong.get_text())
    fship=items[i].find("div",{"class":"icon"}).img
    
    if fship:
        if fship["alt"]=='스마일배송':
            if fship.find_next_sibling("img"):
                print(items[i].find("div",{"class":"icon"}).img.find_next_sibling("img")["alt"])
        else:
            print(fship["alt"])


# best_products=soup.find_all("div",{"class":"best-list"})
# products = best_products[1].find_all("li")


# for i in range(200):
#     print(products[i].img["alt"])
#     print(products[i].strong.get_text())


