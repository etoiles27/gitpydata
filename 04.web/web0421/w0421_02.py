from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re


for j in range(2017,2021):
    
    url = "https://search.daum.net/search?w=tot&q="+str(j)+"%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()  
    soup = BeautifulSoup(res.text,"lxml")

    allmovies = soup.find("ol",{"class":"type_plural list_exact movie_list"})
    movies = allmovies.find_all("li")
    for i in range(5):
        movie_titie = movies[i].find("div",{"class":"info_tit"}).a.get_text()
        img_url = movies[i].img["src"]
        movie_rate =  float(movies[i].find("em",{"class":"rate"}).get_text())
        movie_info =   movies[i].find_all("dd",{"class":"cont"})
        movie_cnt = movie_info[2].get_text()
        movie_link = "http://search.daum.net/search"+movies[i].find("div",{"class":"info_tit"}).a["href"]
        if img_url.startswith("//"):
            img_url="https:"+img_url
        
        
        print("영화제목: {}".format(movie_titie))
        print("영화평점: {}".format(movie_rate))
        print("누적관객: {}".format(movie_cnt))
        # print("영화이미지: {}".format(img_url))
        print("영화링크: {}".format(movie_link))
        
        # 이미지 링크를 가지고 request 파싱
        img_res = requests.get(img_url)
        res.raise_for_status() 
        with open("movie{}_{}.jpg".format(j,i+1),"wb") as f:
            f.write(img_res.content) # request에서 return : status_code 상태, text 글자, content 파일