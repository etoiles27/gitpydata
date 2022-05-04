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

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
# 화면 열지 않고 실행
options.headless = True
options.add_argument("window-size=1920x1080")
userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
options.add_argument(userAgent)


browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.get(url)


elem = browser.find_element_by_id('detected_value')
print(elem.text)
print(userAgent)

browser.quit()