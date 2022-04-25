import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#key 동작 라이브러리
from selenium.webdriver.common.keys import Keys


url = 'https://www.naver.com'
browser = webdriver.Chrome('C:\pydata\chromedriver.exe')
browser.get(url=url)

elem = browser.find_element_by_id("query")
elem.send_keys("시가총액")
elem.send_keys(Keys.ENTER)
elem=browser.find_element_by_partial_link_text("시가총액 상위종목 더보기")