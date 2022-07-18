from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time    # 대기시간 사용을 위해 import
import random  # 랜덤으로 input에 데이터 입력을 위해 import
import pyautogui


# 출력화면이 나타날때까지 대기하는 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# 브라우저 화면의 상태를 알려주는 라이브러리
from selenium.webdriver.support import expected_conditions as EC



# webdriver 크롬브라우저 변수 할당 
options = webdriver.ChromeOptions()
# 브라우저 종료되지 않게 하는 options
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

# 브라우저에서 url사이트를 실행
url = "http://corners.auction.co.kr/corner/UsedMarket.aspx?category=7880000"

href="http://itempage3.auction.co.kr/DetailView.aspx?ItemNo=C658825736&scoredtype=0"

href="http://itempage3.auction.co.kr/DetailView.aspx?ItemNo=C658840218&scoredtype=0"


# 윈도우 창 최대화
# browser.maximize_window()
browser.get(url)

aa = browser.find_element_by_xpath('//*[@id="ucItemList_photoview"]/div/ul[1]/li[1]/div[2]/a')
aa.click()

print('-----------------')
print(aa)

# 탭 이동. 
time.sleep(random.uniform(1,3))
browser.switch_to.window(browser.window_handles[-1])


# #스크롤내림
prev_height = browser.execute_script("return document.body.scrollHeight")
# 무한반복
while True:
    # 자바스크립트 실행 - 스크롤을 아래방향으로 이동시켜줌.
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # scroll(+) 위쪽으로 스크롤  scroll(-) 아래쪽으로 스크롤
    pyautogui.moveTo(500,500)
    pyautogui.scroll(-prev_height)
    # 모니터 해상도의 절대 값을 사용하여 옮길 수 있다. 
    # pyautogui.moveTo(200,200)
    
    # 페이지 열리는 동안 대기
    time.sleep(2)
    # 변경후 높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 스크롤 크기가 더 이상 변경이 없을시 종료
    prev_height = curr_height
    
    
    
    
page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

title = soup.find('h1',{'class':'itemtit'})
if not title:
    title = soup.find('h2',{'class':'hdivItemTitle'})

price = soup.find('strong',{'class':'price_real'})

if not price :
    price = soup.find('span',{'class':'present_num'})
    

txt = browser.find_element_by_xpath('//*[@id="hdivDescription"]/p[1]')

if not txt:
    txt = soup.find('div',{'class':'noticenew'})



print(title)
print(price)
print(txt.text)