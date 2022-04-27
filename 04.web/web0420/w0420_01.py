import requests
from bs4 import BeautifulSoup

def printPage(tr):
    avg = 0 
    for i , cartoon in enumerate(tr):
        title = cartoon.find("td",{"class":"title"})
        if not title:
            continue
        star=cartoon.find("div",{"class":"rating_type"}).strong.get_text()
        avg += float(star)
        
        # print(tr[i].img["src"])
        print(cartoon.find("td",{"class":"title"}).a.get_text(), end='\t')
        print(star, end='\t')
        print(cartoon.find("td",{"class":"num"}).get_text())
        totallist.append(float(star))

    print("페이지 평균평점: {:.2f}".format(avg/(len(tr)-1)) )
    
    

headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
totallist=[]
pagecount = 5

for i in range(1,pagecount+1):
    url= "https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu&page="+str(i)
    res = requests.get(url,headers=headers)
    res.raise_for_status()  
    soup = BeautifulSoup(res.text,"lxml")
    tr = soup.find_all('tr')
    printPage(tr)
    
sum =0
for j in range(len(totallist)):
    sum += totallist[j]
print("전체 평균평점: {:.2f}".format(sum/len(totallist)) )
    



