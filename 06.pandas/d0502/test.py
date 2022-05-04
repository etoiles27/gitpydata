from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup
import time
import re
import random


import pandas as pd


url = 'https://race.kra.co.kr/dbdata/textData.do?Act=12&Sub=1&meet=1'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
options.add_argument(userAgent)

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

browser.find_element_by_xpath('//*[@id="contents"]/ul/li[3]/ul/li[1]/a').click()
time.sleep(2)
txt_url = browser.find_element_by_xpath('//*[@id="inputVo"]/div[1]/table/tbody/tr[1]/td[1]/a').get_attribute('href')
time.sleep(2)

# url 모든 정보를 가져온다

df = pd.read_csv(txt_url, encoding='euc-kr')

df.to_csv('test.csv',encoding='utf-8-sig')