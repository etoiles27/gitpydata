from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import requests
from bs4 import BeautifulSoup
import time
import re
import random

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

url = 'https://www.coupang.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
options.add_argument(userAgent)
# options.add_argument('incognito')
# options.add_argument('headless')
# options.add_argument("no-sandbox")
# options.add_argument("log-level=3")
# options.add_argument('disable-logging' )
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-infobars") 
# options.add_argument("disable-extensions")


# options.add_argument("disable-gpu")
# options.add_argument("lang=ko_KR") # 한국어!
# # options.add_argument("proxy-server=localhost:8080")
# options.add_argument('start-fullscreen')
# options.add_experimental_option("prefs", {
#   "download.default_directory": 'C:\pydata',
#   "download.prompt_for_download": False,
#   "download.directory_upgrade": True,
#   "safebrowsing.enabled": True
# })
# dc = DesiredCapabilities.CHROME
# dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
# os.environ['WDM_LOG_LEVEL'] = '0'
# options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
# options.add_experimental_option("useAutomationExtension", False) 
# options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})



browser = webdriver.Chrome(chrome_options=options)
browser.maximize_window()
# browser.get('about:blank')
# browser.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
# browser.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
# browser.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })




browser.get(url)



time.sleep(random.uniform(1,3))
# #스크롤내림
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
    time.sleep(random.uniform(1,3))
    # 페이지 열리는 동안 대기
    # time.sleep(2)
    # 변경후 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height
    
    
time.sleep(random.uniform(1,3))



page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")


digital = soup.find('div',{'id':'categoryBest_digital'}).a['href']
womanfashion = soup.find('div',{'id':'categoryBest_womanclothe'}).a['href']


digital_url = 'https://www.coupang.com'+digital
womanfashion_url = 'https://www.coupang.com'+womanfashion



browser.find_element_by_xpath('//*[@id="categoryBest_digital"]/dl[1]/dt/a').click()
time.sleep(3)
browser.switch_to.window(browser.window_handles[-1])
digital_product_name=browser.find_element_by_xpath('//*[@id="169628090"]/a/dl/dd/div[2]').text
print(digital_product_name)
time.sleep(3)
browser.close()

browser.switch_to.window(browser.window_handles[0])

browser.find_element_by_xpath('//*[@id="categoryBest_womanclothe"]/dl[1]/dt/a').click()
time.sleep(3)
browser.switch_to.window(browser.window_handles[-1])
womanfashion_product_name=browser.find_element_by_xpath('//*[@id="174997928"]/a/dl/dd/div[2]').text
print(womanfashion_product_name)
time.sleep(3)

browser.quit()
