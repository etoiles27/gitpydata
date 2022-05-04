
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
import random
import re
import csv
import pyautogui
import smtplib
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from fileinput import filename

# 네이버 부동산 -> 공덕삼성 검색 -> 신공덕삼성래미안1차 선택
# 매매 물건 50번째를 출력하세요 

url = 'https://www.naver.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
# options.headless = True
userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
options.add_argument(userAgent)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.maximize_window()
browser.get(url)

time.sleep(random.uniform(1,3))
browser.find_element_by_link_text('부동산').click()
time.sleep(random.uniform(1,3))
browser.find_element_by_id('queryInputHeader').send_keys('공덕삼성',Keys.ENTER)
time.sleep(random.uniform(1,3))
browser.find_element_by_xpath('//*[@id="ct"]/div[2]/div[1]/div[2]/div/div/div[2]/div/a').click()

time.sleep(random.uniform(2,5))

# #스크롤내림
prev_height = browser.execute_script("return articleListArea.scrollHeight")
# 무한반복
while True:
    pyautogui.moveTo(390,1005)
    pyautogui.scroll(-prev_height)
    time.sleep(2)
    curr_height = browser.execute_script("return articleListArea.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height




page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")


houses = soup.find('div',{'id':'articleListArea'}).find_all('div',{'class':'item_inner'})

# print(houses[49])
cnt = 0 
for i in range(len(houses)):
    title = houses[i].find('div',{'class':'item_title'}).span
    price_type = houses[i].find('div',{'class':'price_line'}).span
    price_price = houses[i].find('div',{'class':'price_line'}).find('span',{'class':'price'})
    house_info = houses[i].find('div',{'class':'info_area'})
    if price_type:
        if price_type.get_text()=='매매':
            cnt += 1
            if cnt == 50:
                print(i+1)
                print(title.get_text())
                print(price_type.get_text())
                print(price_price.get_text())
                print(house_info.get_text())

                



browser.close()