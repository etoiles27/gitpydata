import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
import random
import pyautogui
import re
import csv

url = 'https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Nov0920&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Nov0920-Text_Search_BKWS-BKWS%7cONSEM_kwid_43700058444564844_creativeid_477193019447_device_c&gclid=EAIaIQobChMI4dHfjMCw9wIVCjdgCh2s5AS1EAAYASAAEgK-YfD_BwE&gclsrc=aw.ds'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
# 화면 열지 않고 실행
options.headless = True
options.add_argument("window-size=1920x1080")
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.get(url)

filename = 'movie.csv'
f = open(filename, 'w',encoding='utf-8',newline='')
writer= csv.writer(f)
writer.writerow(['제목','평점','가격'])
# 자동 스크롤 using javascript 
prev_height = browser.execute_script("return document.body.scrollHeight")

# 무한반복
while True:
    # 자바스크립트 실행 - 스크롤을 아래방향으로 이동시켜줌.
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # scroll(+) 위쪽으로 스크롤  scroll(-) 아래쪽으로 스크롤
    # pyautogui.moveTo(500,500)
    # pyautogui.scroll(-prev_height)
    # 모니터 해상도의 절대 값을 사용하여 옮길 수 있다. 
    # pyautogui.moveTo(200,200)
    
    # 페이지 열리는 동안 대기
    time.sleep(2)
    # 변경후 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height
    # 무한반복 끝


# 화면캡쳐 
browser.get_screenshot_as_file('googleMovie_sh.jpg')

page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")


# headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
#          'Accept-Language':'ko-KR,ko'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() 

# soup = BeautifulSoup(res.text,"lxml")

# 제목 평점 금액
lists = soup.find_all('section')#.find_all('div',{'class':'ULeU3b neq64b'})

fam_movies = lists[9].find_all('div',{'class':'ULeU3b neq64b'})


for i in range(len(fam_movies)):
    tmp = []
    cons = fam_movies[i].find('span',{'class':'VfPpfd VixbEe'}).span.get_text()
    cons = int(re.sub(r'[^0-9]','',cons))

    # cons = int(cons[1:].replace(',',''))
    
    
    if cons<=6000:
        
        title = fam_movies[i].find('div',{'class':'hP61id'}).div['title']
        star = fam_movies[i].find('div',{'class':'LrNMN'}).get_text()
        star = float(re.sub(r'[^0-9.]','',star))
        poster = fam_movies[i].find('div',{'class':'TjRVLb'}).img['src']
        img_res = requests.get(poster)
        mov =''
        if fam_movies[i].find('div',{'class':'TjRVLb'}).button:
            mov = fam_movies[i].find('div',{'class':'TjRVLb'}).button['data-trailer-url']
        #price = fam_movies[i].find('span',{'class':'VfPpfd VixbEe'}).span.get_text()
        print('{}위'.format(i+1))      
        print('영화 제목: {}'.format(title))
        print('영화 별점: {}'.format(star))
        print('영화 가격: {}원'.format(cons))
        print('영화 영상: {}'.format(mov))
        with open("poster{}.jpg".format(i+1),"wb") as f:
            f.write(img_res.content)
        
        tmp=[title, star, cons]
        writer.writerow(tmp)
        
        
f.close()

time.sleep(4)

# browser.close()
browser.quit()