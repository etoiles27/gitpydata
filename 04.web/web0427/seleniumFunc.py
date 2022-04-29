from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
import random
import re
from saveall import * 



def openbrowser(url):
    url = url
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach',True)
    userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    options.add_argument(userAgent)
    browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
    browser.get(url)
    return browser
    


def searchNaverWithlinkText(sec):
    
    url = 'https://www.naver.com/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach',True)
    userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    options.add_argument(userAgent)
    browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
    browser.get(url)
    browser.find_element_by_link_text(sec).click()
    page_url = browser.page_source
    soup = BeautifulSoup(page_url,"lxml")
    return browser, soup

def searchNaverByInsertTxt(txt):
    url = 'https://www.naver.com/'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach',True)
    userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    options.add_argument(userAgent)
    browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
    browser.get(url)
    browser.find_element_by_id('query').send_keys(txt,Keys.ENTER)
    time.sleep(random.uniform(1,3))
    page_url = browser.page_source
    soup = BeautifulSoup(page_url,"lxml")
    return browser, soup

def closeBrowser(browser):
    browser.quit()



def melonTop100(soup,fn):
    charts = soup.find('tbody').find_all("tr")
    f, writer = openCSV(fn)
    writer.writerow(['순위','제목','가수','앨범','좋아요'])
    for i in range(len(charts)):
        tmp =[]
        rank = i+1
        song_title = charts[i].find('div',{'class':'ellipsis rank01'}).span.a
        song_singer = charts[i].find('div',{'class':'ellipsis rank02'}).a
        album = charts[i].find('div',{'class':'ellipsis rank03'}).a
        like = charts[i].find('span',{'class':'cnt'})
        
        if like:
            like_num = re.sub('[^0-9,]','',like.get_text())
            print('{}위'.format(rank))
            print('제목 : {}'.format(song_title.get_text()))
            print('가수 : {}'.format(song_singer.get_text()))
            print('앨범 : {}'.format(album.get_text()))
            print('좋아요: {}'.format(like_num))
            tmp = [rank,song_title.get_text(),song_singer.get_text(),album.get_text(),like_num]
            writer.writerow(tmp)
    closeFile(f)        