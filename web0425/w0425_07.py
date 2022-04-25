from xml.dom.minidom import Document
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
#key 동작 라이브러리
from selenium.webdriver.common.keys import Keys
import time # 대기시간 사용을 위해 import
import random #랜덤으로 input에 데이터 입력을 위해 import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 크롬브라우져 생성 및 페이지 이동 
# option 으로 화면 바로 안꺼지게- 
url = 'https://flight.naver.com/flights/domestic/SEL-CJU-20220524/CJU-SEL-20220525?adult=2&fareType=YC'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
# 최대화면 
browser.maximize_window()
browser.get(url=url)



WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]')))

# 자동 스크롤 using javascript 
prev_height = browser.execute_script("return document.body.secollHeight")
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    curr_height = browser.execute_script("return document.body.secollHeight")

    if prev_height == curr_height:
        break
    prev_height = curr_height
    

page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")
flights = soup.find('div',{'class':'domestic_results__yNAgI'}).find_all('div',{'class':'domestic_Flight__sK0eA result'})

print(len(flights))