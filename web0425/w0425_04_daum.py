import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#key 동작 라이브러리
from selenium.webdriver.common.keys import Keys


url = 'https://www.daum.net'
browser = webdriver.Chrome('C:\pydata\chromedriver.exe')
browser.get(url=url)

elem = browser.find_element_by_id('q').send_keys("부동산").send_keys(Keys.ENTER)
