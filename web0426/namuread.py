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
import smtplib #메일발송라이브러리
from email.mime.text import MIMEText # 글자를 보낼 때 사용한다. 

# 구글에서 검색=> 기사를 찾아 메일 보내기 


url = 'https://namu.wiki/w/%EC%84%B8%EC%A2%85'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.get(url)


elem = browser.find_element_by_xpath('//*[@id="xe3YJFkGZ"]/article/div[3]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div/div/div[8]/div[1]/div/div[4]')
print(elem.text)