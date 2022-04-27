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

url = 'https://www.yanolja.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.maximize_window()
browser.get(url)

filename = 'hotels.csv'
f = open(filename, 'w',encoding='utf-8',newline='')
writer= csv.writer(f)
writer.writerow(['호텔명','가격','평점','링크'])

browser.find_element_by_class_name('HomeSearchBar_search__3R15k').click()
# 검색창에 제주리조트 검색어 삽입

elem = browser.find_element_by_class_name('SearchInput_input__342U2').send_keys('제주리조트',Keys.ENTER)


time.sleep(random.uniform(1,3))

# # 날짜 5.27-5.28
elem = browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/div[1]/header/div/section/div/div[3]/button[1]')
elem.click()
time.sleep(random.uniform(1,3))
elem = browser.find_element_by_xpath('/html/body/div[5]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[6]')
time.sleep(random.uniform(1,2))
elem.click()
time.sleep(random.uniform(1,2))
elem = browser.find_element_by_xpath('/html/body/div[5]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[7]')
time.sleep(random.uniform(1,2))
elem.click()
time.sleep(random.uniform(1,2))
elem = browser.find_element_by_xpath('/html/body/div[5]/div/div/section/section[4]/button')
time.sleep(random.uniform(1,2))
elem.click()
time.sleep(random.uniform(1,3))

# #스크롤내림
prev_height = browser.execute_script("return document.body.scrollHeight")
# 무한반복
while True:
    # 자바스크립트 실행 - 스크롤을 아래방향으로 이동시켜줌.
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # scroll(+) 위쪽으로 스크롤  scroll(-) 아래쪽으로 스크롤
    pyautogui.moveTo(500,500)
    pyautogui.scroll(-prev_height)
    # 모니터 해상도의 절대 값을 사용하여 옮길 수 있다. 
    # pyautogui.moveTo(200,200)
    
    # 페이지 열리는 동안 대기
    time.sleep(2)
    # 변경후 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height
    
    
    
    

# 페이지 soup 가져오기
url = browser.current_url
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

hotels = soup.find_all('div',{'class':'PlaceListItemText_container__fUIgA'})

# 평점 4.0점이상, 제목, 평점, 금액, 링크 

# hotel_name = hotels[0].find('strong',{'class':'PlaceListTitle_text__2511B small'})
# hotel_price = hotels[0].find('span',{'class':'PlacePriceInfo_salePrice__28VZD'})
# hotel_rate = hotels[0].find('span',{'class':'PlaceListScore_rating__3Glxf'})
# hotel_link = hotels[0].a




for i in range(len(hotels)):
    temp=[]
    hotel_name = hotels[i].find('strong',{'class':'PlaceListTitle_text__2511B small'})
    hotel_price = hotels[i].find('span',{'class':'PlacePriceInfo_salePrice__28VZD'})
    hotel_rate = hotels[i].find('span',{'class':'PlaceListScore_rating__3Glxf'})
    hotel_link = hotels[i].a
    hotel_img = hotels[i].find('div',{'class':'PlaceListImage_imageText__2XEMn'})
    
    
    if hotel_rate:
        hotel_rate_float = float(hotel_rate.get_text())
        
        if hotel_rate_float>4.0:
            print('호텔 이름 : {}'.format(hotel_name.get_text()))
            print('호텔 가격 : {}'.format(hotel_price.get_text()))
            print('호텔 평점 : {}'.format(hotel_rate.get_text()))
            print('호텔 링크 : {}'.format('https://www.yanolja.com'+hotel_link['href']))
            n = hotel_img["style"].find("https://")
            hotel_img_url = hotel_img["style"][n:-3]
            temp=[hotel_name.get_text(),hotel_price.get_text(),hotel_rate.get_text(),'https://www.yanolja.com'+hotel_link['href']]
            writer.writerow(temp)
            # img_res = requests.get(hotel_img_url)
            # with open("hotel{}.jpg".format(i+1),"wb") as f:
            #     f.write(img_res.content)
    
f.close()