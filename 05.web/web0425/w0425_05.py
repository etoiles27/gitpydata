import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#key 동작 라이브러리
from selenium.webdriver.common.keys import Keys



# url = "https://finance.naver.com/"
# headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status() 

url = 'https://www.naver.com/'
browser = webdriver.Chrome('C:\pydata\chromedriver.exe')
browser.get(url=url)

# elem = browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[3]/a').send_keys(Keys.ENTER)
elem = browser.find_element_by_link_text('증권').send_keys(Keys.ENTER)

# 현재페이지url가져오기
page_url = browser.page_source

soup = BeautifulSoup(page_url,"lxml")

with open("elum.html",'w',encoding='utf-8') as f:
    f.write(soup.prettify())