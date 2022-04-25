import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#key 동작 라이브러리
from selenium.webdriver.common.keys import Keys


# request 로는 멜론에 있는 좋아요 수를 찾을 수 없다 
# urlreq = "https://www.melon.com/chart/index.htm"
# headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
# res = requests.get(urlreq,headers=headers)
# res.raise_for_status() 

# soupreq = BeautifulSoup(res.text,"lxml")

# charts = soupreq.find('tbody').find_all("tr",{"id":"lst50"})
# print(charts[0].find("div",{"class":"ellipsis rank03"}).get_text())
# print(charts[0].find("span",{"class":"cnt"})) # 좋아요 숫자가 0으로 나옴


url = 'https://www.melon.com/chart/index.htm'
browser = webdriver.Chrome('C:\pydata\chromedriver.exe')
browser.get(url=url)

# 현재페이지url가져오기
page_url = browser.page_source

soup = BeautifulSoup(page_url,"lxml")

charts = soup.find('tbody').find_all("tr",{"id":"lst50"})
print(charts[0].find("span",{"class":"cnt"})) 
