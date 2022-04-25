import requests
from selenium import webdriver
#key 동작 라이브러리
from selenium.webdriver.common.keys import Keys

url = 'https://www.naver.com'
browser = webdriver.Chrome()
browser.get(url=url)

elem = browser.find_element_by_class_name("link_login")
elem.click()

elem = browser.find_element_by_id("id")
elem.send_keys("aaa")
elem=browser.find_element_by_xpath('//*[@id="pw"]')
elem.send_keys("1111")

elem.click()



browser.back()
browser.forward()
browser.refresh()



# from bs4 import BeautifulSoup
# url = 'https://www.naver.com'
# headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()  
# soup = BeautifulSoup(res.text,"lxml")