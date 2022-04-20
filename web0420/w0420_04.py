import requests
from bs4 import BeautifulSoup
import re


headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}



productlists =[]
pagecnt=5
for i in range(1,(pagecnt)):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+str(i)
    res = requests.get(url,headers=headers)
    res.raise_for_status()  
    soup = BeautifulSoup(res.text,"lxml")
    items = soup.find_all("li",{"class":"search-product"})
    
    for i, item in enumerate(items):
        productjason={}
        product_name=""
        if item.find("div",{"class":"name"}):
            product_name = item.find("div",{"class":"name"}).get_text()  # 제품명
        rate=0
        if item.find("em",{"class":"rating"}):
            rate = float(item.find("em",{"class":"rating"}).get_text()) # 평점
        rate_cnt=0
        rate_cnt_added=0
        if item.find("span",{"class":"rating-total-count"}):
            rate_cnt_added = item.find("span",{"class":"rating-total-count"}).get_text() # 상품평
            rate_cnt = int(rate_cnt_added[1:-1])
        price=""
        if item.find("strong",{"class":"price-value"}):
            price =item.find("strong",{"class":"price-value"}).get_text() # 제품가격
        link = "https://www.coupang.com"+item.a["href"]
        isad="no"
        if item.find("span",{"class":"ad-badge-text"}):
            isad="yes"
        productjason={"name":product_name,"rate":rate,"rateCnt":rate_cnt,"price":price,"link":link,"ad":isad}
        productlists.append(productjason)
        

print(productlists)

print("*"*20)

cnt = 0 
for i in range(len(productlists)):
    if(productlists[i]['rate']>=4.5) and productlists[i]['rateCnt']>=100 and productlists[i]['ad'] == "no" :
        if not 'Apple' in productlists[i]['name']:
            cnt+=1
            print(cnt,".")
            print("제품명 : {}".format(productlists[i]['name']))
            print("금액 : {}".format(productlists[i]['price']))
            print("평점 : {}".format(productlists[i]['rate']))
            print("상품평 : {}".format(productlists[i]['rateCnt']))
            print("링크 : {}".format(productlists[i]['link']))
            
            # print(productlists[i])






# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+str(1)
# res = requests.get(url,headers=headers)
# res.raise_for_status()  
# soup = BeautifulSoup(res.text,"lxml")



#items = soup.find_all("li",{"class":re.compile("^search-product")})
# items = soup.find_all("li",{"class":"search-product"})
# product_name = items[0].find("div",{"class":"name"}).get_text()  # 제품명
# rate = float(items[0].find("em",{"class":"rating"}).get_text()) # 평점
# rate_cnt_added = items[0].find("span",{"class":"rating-total-count"}).get_text() # 상품평
# rate_cnt = int(rate_cnt_added[1:-1])
# price =items[0].find("strong",{"class":"price-value"}).get_text() # 제품가격


# print(product_name)  
# print(rate) 
# print(rate_cnt) 
# print(price)
