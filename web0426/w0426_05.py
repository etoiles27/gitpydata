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


url = 'https://www.google.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.get(url)


time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('한소희',Keys.ENTER)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="rso"]/div[6]/div/div[1]/div/div/div[1]/div[1]/div/a').click()
time.sleep(2)


elem = browser.find_element_by_id('article_body')
print(elem.text)
time.sleep(2)




smtpName ="smtp.naver.com"
smtpPort = 587

sendEmail = 'rimicom@naver.com'
password = 'gkflagkfla'
recvEmail = sendEmail
#recvEmail = 'xnmx1234@naver.com'

title = '[한소희]파이썬 이메일 보내기 수업'
content =elem.text

msg = MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['subject']=title

s=smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,password)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.close()