import requests
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

import smtplib
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from fileinput import filename

url = 'https://www.naver.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
options.add_argument(userAgent)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.get(url)



#  네이버>증권>주요뉴스
#  제목, 링크주소 6개 
browser.find_element_by_link_text('증권').click()
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[1]/div/ul/li[1]/span/a')
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")
news = soup.find('div',{'class':'section_strategy'}).find_all('li')


for i in range(len(news)):
    title = news[i].a.get_text()
    link = 'https://finance.naver.com/' + news[i].a['href']
    print('{}.'.format(i+1))
    print('뉴스 제목 : ', title)
    print('뉴스 링크 :', link)
    
time.sleep(random.uniform(1,3))
# 주식정보 . 금융검색: 삼성전자
#  종목명 현재가 전일대비 등락율 매도호가 매수호가 거래량 거래대금
browser.find_element_by_id('stock_items').send_keys('삼성전자',Keys.ENTER)
time.sleep(random.uniform(1,3))
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

stock_info = soup.find('table').find_all('td')

print('종목명         :{}'.format(stock_info[0].get_text().strip()))
print('현재가         :{}'.format(stock_info[1].get_text()))
print('전일대비       :{}'.format(stock_info[2].get_text()))
print('등락율         :{}'.format(stock_info[3].get_text()))
print('매도호가       :{}'.format(stock_info[4].get_text()))
print('매수호가       :{}'.format(stock_info[5].get_text()))
print('거래량         :{}'.format(stock_info[6].get_text()))
print('거래대금(백만) :{}'.format(stock_info[7].get_text()))

# 네이버 메인으로 
time.sleep(random.uniform(1,3))
browser.find_element_by_class_name('logo_naver').click()
time.sleep(random.uniform(1,3))

    
    
# 네이버 날씨 주간예보 - 오늘 오전 맑음10/21 내일 맑음 흐림 11/22 
browser.find_element_by_id('query').send_keys('날씨',Keys.ENTER)
time.sleep(random.uniform(1,3))
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")
week_weather = soup.find('ul',{'class':'week_list'}).find_all('li')

for i in range(0,2):

    today_day = week_weather[i].find('strong',{'class':'day'}).get_text()
    today_date = week_weather[i].find('span',{'class':'date'}).get_text()
    today_weather = week_weather[i].find_all('span',{'class':'weather_inner'})
    today_morning = today_weather[0].i.get_text()
    today_afternoon = today_weather[1].i.get_text()
    today_lowtemp = week_weather[i].find('span',{'class':'lowest'}).get_text()
    today_hightemp = week_weather[i].find('span',{'class':'highest'}).get_text()


    print(today_day, today_date)
    print('오전: {}, 오후: {}'.format(today_morning,today_afternoon))
    print(today_lowtemp,today_hightemp)


# 멜론 파일첨부 1-100위까지 csv 파일 저장 
# 순위 곡정보(제목,가수) 앨범, 좋아요
time.sleep(random.uniform(1,3))
browser.find_element_by_class_name('link').click()
time.sleep(random.uniform(1,3))
browser.find_element_by_id('query').send_keys('멜론',Keys.ENTER)
time.sleep(random.uniform(1,3))
browser.find_element_by_class_name('link_name').click()
time.sleep(random.uniform(1,3))
browser.find_element_by_link_text('멜론차트').click()
time.sleep(random.uniform(1,3))


# 멜론 차트페이지 이동. 
# 현재 browser을 현재 탭으로 설정. 
browser.switch_to.window(browser.window_handles[-2])
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

# csv 저장 
filenameA = 'aaa.csv'
f = open(filenameA,'w',encoding='utf-8-sig',newline='')
writer = csv.writer(f)

writer.writerow(['순위','제목','가수','앨범','좋아요'])

charts = soup.find('tbody').find_all("tr")

for i in range(len(charts)):
    tmp =[]
    rank = i+1
    song_title = charts[i].find('div',{'class':'ellipsis rank01'}).span.a
    song_singer = charts[i].find('div',{'class':'ellipsis rank02'}).a
    album = charts[i].find('div',{'class':'ellipsis rank03'}).a
    like = charts[i].find('span',{'class':'cnt'})
    
    if like:
        like_num = re.sub('[^0-9,]','',like.get_text())
        # print('{}위'.format(rank))
        # print('제목 : {}'.format(song_title.get_text()))
        # print('가수 : {}'.format(song_singer.get_text()))
        # print('앨범 : {}'.format(album.get_text()))
        # print('좋아요: {}'.format(like_num))
        tmp = [rank,song_title.get_text(),song_singer.get_text(),album.get_text(),like_num]
        writer.writerow(tmp)
        
f.close()        

# selenium 종료
browser.quit() 


# 메일보내기 
smtpName ="smtp.naver.com"
smtpPort = 587

sendEmail = 'ㅁㅁ@naver.com'
password = '1111'
recvEmail = sendEmail


title = '[python] 첨부파일 '
content = 'string'


# MIME 객체생성
msg = MIMEMultipart('alternative')
# msg = MIMEText(content)
part2= MIMEText(content)
msg.attach(part2)
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subject'] = title

#파일첨부
part = MIMEBase('application',"octet-stream")
#파일읽어오기
with open('aaa.csv',"rb") as f:
    #part에 파일담기
    part.set_payload(f.read())

# 파일첨부할수 있는 형태로 인코딩
encoders.encode_base64(part) 

#header정보 정의
part.add_header('Content-Dispostion','attachment',filename='aaa.csv')   

# content,첨부파일을 attach추가
msg.attach(part)

# 메일서버 정보
s = smtplib.SMTP(smtpName,smtpPort)
s.starttls() # 서버접근
s.login(sendEmail,password) #서버로그인
# 메일 발송(보내는주소,받는주소,내용)
s.sendmail(sendEmail,recvEmail,msg.as_string())
print("메일발송이 완료되었습니다.")
s.close()




