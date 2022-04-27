from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time 
import random
import re
import csv

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

