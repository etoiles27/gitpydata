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


smtpName ="smtp.naver.com"
smtpPort = 587

sendEmail = 'rimicom@naver.com'
password = 'gkflagkfla'
recvEmail = 'xnmx1234@naver.com'

title = '파이썬 이메일 보내기 수업'
content ='파이썬 수업이 진행중입니다. 현재 38일차 입니다.'

msg = MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['subject']=title

s=smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,password)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.close()