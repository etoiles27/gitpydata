import requests
from bs4 import BeautifulSoup
import re





url = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220421&hh=15&rtm=Y&pg={}".format(1)
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")
musics = soup.find_all("tr",{"class":"list"})
# music_title = musics[19].find("a",{"class":"title ellipsis"}).get_text().strip()
# if  musics[20].find("a",{"class":"title ellipsis"}).find("span"):
#     music1 =  musics[20].find("a",{"class":"title ellipsis"}).find("span").next_sibling.strip()
#     print(music1)
# else:
#     print(music_title)
    
    

cnt=0
for page in range(1,5):
    
    url = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220421&hh=15&rtm=Y&pg={}".format(page)
    headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()  
    soup = BeautifulSoup(res.text,"lxml")
    musics = soup.find_all("tr",{"class":"list"})
    


    for music in musics:
        get_music_title = music.find("a",{"class":"title ellipsis"}) # music.find("a",{"class":"albumtitle ellipsis"}).get_text()
        if get_music_title.find("span"):
            music_title = get_music_title.find("span").next_sibling.strip()
        else:
            music_title = get_music_title.get_text().strip()
        
        music_singer= music.find("a",{"class":"artist ellipsis"}).get_text()
        music_imgurl = "https:"+music.find("a",{"class":"cover"}).img["src"]
        cnt+=1
        print("{}위.".format(cnt))
        print("음악제목: {}".format(music_title))
        print("음악가수: {}".format(music_singer))
        print("앨범이미지: {}".format(music_imgurl))
        # music_imgurl_res = requests.get(music_imgurl)
        # with open("img_{}.jpg".format(cnt),"wb") as f:
        #     f.write(music_imgurl_res)