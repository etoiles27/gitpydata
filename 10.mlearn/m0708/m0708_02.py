# 날짜, 금액, text, 폰모델/ 출고가, 제조사/ 이동통신물가지수 => 2000개
# 폰가격 예측
#크롬 웹드라이버 관리 라이브러리 호출

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv 
import time # 대기시간 사용을 위한 import
import random # 랜덤으로 input에 데이터 입력

# 출력화면이 나타날때까지 대기하는 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 라이브러리
from selenium.webdriver.support import expected_conditions as EC
browser=webdriver.Chrome()
url='https://m.bunjang.co.kr/categories/600700001?page='+str(1)+'&order=date'
browser.get(url)

# csv 파일 저장
filename='phone info.csv'
f=open(filename,'w',encoding='utf-8-sig',newline='')

writer=csv.writer(f)

title='폰모델 제목,가격,등록시간,내용'
title=title.split(',')
writer.writerow(title)


# 현재 웹페이지 html소스를 가져옴.
page_html = browser.page_source
# BeautifulSoup html파싱
soup = BeautifulSoup(page_html,"lxml")
divs=soup.find_all('div',{'class':'sc-ejGVNB jrCaJ'})
for div in divs:
    data=[]
    main_url='https://m.bunjang.co.kr'
    url=main_url+div.find('a')['href']
    browser.get(url)
    page_html = browser.page_source
    # BeautifulSoup html파싱
    soup = BeautifulSoup(page_html,"lxml")
    title=soup.find('div',{'class':'sc-jrIrqw deihsD'}).get_text()
    price=soup.find('div',{'class':'sc-iQtOjA beRPoY'}).get_text().split('원')[0]
    price=price.replace(',','')
    price=int(price)
    times=soup.find('div',{'class':'sc-fyjhYU dRDSys'}).find('div',{'class':'sc-ugnQR bHzOsq'}).find('div',{'class':'sc-eIHaNI kvuSXN'})
    time1=times.find_all('div',{'class':'sc-eTpRJs jbRTcu'})[2].get_text()
    context=str(soup.find('div',{'class':'sc-eLdqWK evwfQs'}).get_text()).split('\n')
    context2=''
    for con in context:
        context2+=con
    
    data.append(title)
    data.append(price)
    data.append(time1)
    data.append(context2)
    writer.writerow(data)

f.close()
    