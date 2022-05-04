from xml.dom.minidom import Document
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#key 동작 라이브러리
from selenium.webdriver.common.keys import Keys
import time # 대기시간 사용을 위해 import
import random #랜덤으로 input에 데이터 입력을 위해 import

# 크롬브라우져 생성 및 페이지 이동
url = 'https://www.naver.com'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.get(url=url)


browser.find_element_by_class_name("link_login").click()

# 대기시간을 적용, 랜덤으로 1초~3초 사이 시간을 대기함 
time.sleep(random.uniform(2,5))

input_js = "document.getElementById('id').value='{id}';\
    document.getElementById('pw').value='{pw}'\
        ".format(id='rimicom',pw='gkflagkfla')


browser.execute_script(input_js)

time.sleep(random.uniform(2,5))
browser.find_element_by_id("log.login").click()


#browser.find_element_by_class_name("num MY_MAIL_COUNT").click()

browser.find_element_by_link_text("메일").click()

browser.find_element_by_link_text('메일쓰기').click()


browser.find_element_by_id('toInput').send_keys('onulee@naver.com')
browser.find_element_by_id('subject').send_keys('[test]자동 메일입니다.')
browser.find_element_by_xpath('/html/body').send_keys('[test]내용')

browser.find_element_by_id("se2_iframe").send_keys('[test]내용')

browser.find_element_by_id('sendBtn').click()