
import requests
from bs4 import BeautifulSoup
from sendmail import *
from seleniumFunc import *
from saveall import * 
import pyautogui



url = 'https://images.google.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
options.add_argument(userAgent)
browser = webdriver.Chrome('C:\pydata\chromedriver.exe',options=options)
browser.get(url)
time.sleep(random.uniform(1,3))
browser.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input').send_keys('한소희',Keys.ENTER)


# cnt = 0
# # #스크롤내림
# prev_height = browser.execute_script("return document.body.scrollHeight")
# # 무한반복
# while True:
#     pyautogui.moveTo(390,1005)
#     pyautogui.scroll(-prev_height)
#     time.sleep(2)
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if prev_height == curr_height:
#         break # 스크롤 크기가 더 이상 변경이 없을시 종료
#     prev_height = curr_height
#     cnt+=curr_height
    
# pyautogui.scroll(cnt)



for i in range(3):
    time.sleep(random.uniform(1,3))
    browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i+1) +']/a[1]').click()
    time.sleep(random.uniform(1,3))
    img_url = browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute('src')
    time.sleep(random.uniform(1,3))

    headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    img_res = requests.get(img_url)
    res = requests.get(img_url,headers=headers)
    res.raise_for_status() 
    with open('so'+str(i+1)+'.jpg ',"wb") as f:
        f.write(img_res.content)

    browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[2]/a').click()
    time.sleep(random.uniform(1,3))
    
    f.close()
    
print('저장이 완료되었습니다. ')
browser.quit()