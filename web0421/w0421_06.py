from types import coroutine
import requests
from bs4 import BeautifulSoup
import re
import csv



url = "https://www.melon.com/chart/index.htm"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")
# musics = soup.find_all("tr",{"class":"lst50"})
musics = soup.find("tbody").find_all("tr")


cnt=0
mu_info=[]



for music in musics:
    cnt+=1
    rank = cnt
    title = music.find("div",{"class":"ellipsis rank01"}).a.get_text().strip()
    singer = music.find("div",{"class":"ellipsis rank02"}).a.get_text().strip()
    album = music.find("div",{"class":"ellipsis rank03"}).a.get_text().strip()
    # like = music.find("span",{"class":"cnt"})
    
    
    
    print(rank, title, singer,album)