from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

import random


url = 'https://www.coupang.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
options.add_argument(userAgent)

browser = webdriver.Chrome(chrome_options=options)
browser.maximize_window()

# 웹크롤링 접근이 아니라고 강제적으로 입력해주는 명령어라는데.. (구글링으로 ..)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })


browser.get(url)
time.sleep(random.uniform(1,3))
# #스크롤내림
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.uniform(1,3))
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
    
    
time.sleep(random.uniform(1,3))



page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

# url 가져오기
digital = soup.find('div',{'id':'categoryBest_digital'}).a['href']
womanfashion = soup.find('div',{'id':'categoryBest_womanclothe'}).a['href']
digital_url = 'https://www.coupang.com'+digital
womanfashion_url = 'https://www.coupang.com'+womanfashion


# 디지털 클릭하기 
browser.find_element_by_xpath('//*[@id="categoryBest_digital"]/dl[1]/dt/a').click()
time.sleep(3)
# 현재 탭으로 이동
browser.switch_to.window(browser.window_handles[-1])
digital_product_name=browser.find_element_by_xpath('//*[@id="169628090"]/a/dl/dd/div[2]').text
print(digital_product_name)
time.sleep(3)
# 현재 탭 닫기
browser.close()

# 원래 쿠팡페이지로 돌아오기
browser.switch_to.window(browser.window_handles[0])


# 여성패션 클릭하기
browser.find_element_by_xpath('//*[@id="categoryBest_womanclothe"]/dl[1]/dt/a').click()
time.sleep(3)
# 현재 탭으로 이동
browser.switch_to.window(browser.window_handles[-1])
womanfashion_product_name=browser.find_element_by_xpath('//*[@id="174997928"]/a/dl/dd/div[2]').text
print(womanfashion_product_name)
time.sleep(3)
# 전체 창 끄기 
browser.quit()
