import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#key 동작 라이브러리
from selenium.webdriver.common.keys import Keys


url = 'https://www.naver.com'
browser = webdriver.Chrome('C:\pydata\chromedriver.exe')
browser.get(url=url)


elem = browser.find_element_by_id("query")
elem.send_keys("지마켓")
elem = browser.find_element_by_id("search_btn")
elem.click()

elem = browser.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a')
elem.click()