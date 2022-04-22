import requests
from bs4 import BeautifulSoup


# 11번가 best500
# 1-28위
# 제목, 금액, 링크, 무료배송, 사진 저장 및 출력 

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")
items=soup.find("div",{"id":"bestPrdList"}).find("div",{"class":"viewtype catal_ty"}).find_all('li')


print("[ 11번가 best500제품 (1-28위) ]")
print('-'*100)

for i in range(28):
    # 제품명. 존재하면 get_text, 아니면 공백 
    get_title = items[i].find("div",{"class":"pname"}).p
    item_title=''
    if get_title:
        item_title = get_title.get_text().strip()
    # 제품가격. 존재하면 get_text, 아니면 공백    
    get_price = items[i].find("strong",{"class":"sale_price"})
    item_price =''
    if get_price:
        item_price = get_price.get_text().strip()
    # 제품링크. 존재하면 a tag 에 있는 href , 아니면 공백
    get_link = items[i].a
    item_link=''
    if get_link:
        item_link = get_link["href"]
    # 제품이미지. 존재하면 img tag 에 있는 src , 아니면 공백
    get_imgurl = items[i].find("div",{"class":"img_plot"}).img
    item_imgurl = ''
    if get_imgurl:
        item_imgurl = get_imgurl["src"]
    # 무료배송 여부. 무료배송태그가 존재하면 get_text, 아니면 유료
    get_ship = items[i].find("div",{"class":"s_flag"}).em
    item_ship = '유료'
    if get_ship:
        item_ship=get_ship.get_text()

    print("{}위 제품".format(i+1))
    print("제품명   : {}".format(item_title))
    print("제품가격 : {}".format(item_price))
    print("제품링크 : {}".format(item_link))
    print("배송 : {}".format(item_ship))
    # print(item_imgurl)
    
    # 제품사진 저장 
    img_res = requests.get(item_imgurl)
    res.raise_for_status() 
    with open("item{}.jpg".format(i+1),"wb") as f:
        f.write(img_res.content)

f.close()