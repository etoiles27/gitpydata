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
import csv


# 크롬브라우져 생성 및 페이지 이동 
# option 으로 화면 바로 안꺼지게- 
url = 'https://flight.naver.com'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
# 최대화면 
browser.maximize_window()
browser.get(url=url)

# 출발
time.sleep(2)
elem = browser.find_elements_by_class_name('select_code__d6PLz')[0].click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[1]/i[2]').click()
# 도착 
time.sleep(2)
elem = browser.find_elements_by_class_name('select_code__d6PLz')[1].click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]/i[2]').click()

#가는날
time.sleep(2)
# elem = browser.find_elements_by_class_name('tabContent_option__2y4c6 select_Date__1aF7Y')[0].click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[3]/button').click()
# #오는날
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button').click()
time.sleep(2)



browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[3]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[3]/div/div/div[1]/div[1]/button[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[3]/button').click()
time.sleep(2)
browser.find_element_by_class_name('searchBox_txt__3RoCw').click()
# browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()

WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]')))

# 자동 스크롤 using javascript 
prev_height = browser.execute_script("return document.body.scrollHeight")



# 무한반복
while True:
    # 자바스크립트 실행 - 스크롤을 아래방향으로 이동시켜줌.
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 열리는 동안 대기
    time.sleep(2)
    # 변경후 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height
    # 무한반복 끝

    


page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")
flights = soup.find('div',{'class':'domestic_results__yNAgI'}).find_all('div',{'class':'domestic_Flight__sK0eA result'})

print(len(flights))
# flight_name = flights[0].find("b",{'class':'name'}).get_text()
# flight_time = flights[0].find_all("b",{'class':'route_time__-2Z1T'})
# flight_time_to = flight_time[0].get_text()
# flight_time_from = flight_time[1].get_text()
# flight_fair = flights[0].find("i",{'class':'domestic_num__2roTW'}).get_text()
# print(flight_name,flight_time_to,flight_time_from,flight_fair)

f=open('flightfare.csv', 'w',encoding='utf-8-sig',newline='')
writer = csv.writer(f)


for i in range (len(flights)):
    
    mylist =[]
    
    flight_name = flights[i].find("b",{'class':'name'})
    flight_time = flights[i].find_all("b",{'class':'route_time__-2Z1T'})
    flight_time_to = flight_time[0]
    flight_time_from = flight_time[1]
    flight_fair = flights[i].find("i",{'class':'domestic_num__2roTW'})
    
    if flight_fair:
        flight_fair_r =  flight_fair.get_text()
        flight_fair_r = flight_fair_r.replace(',','')
        flight_fair_real = int(flight_fair_r)
        if flight_fair_real<50000:
            print(flight_name.get_text(),flight_time_to.get_text(),flight_time_from.get_text(),flight_fair_real)
            mylist=[flight_name.get_text(),flight_time_to.get_text(),flight_time_from.get_text(),flight_fair_real]
            writer.writerow(mylist)


f.close()
