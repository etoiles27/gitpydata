import requests
from bs4 import BeautifulSoup
from sendmail import *
from selennaver import *
from saveall import * 


# # 증권뉴스 
# browser, soup = searchNaverWithlinkText('증권')
# news = soup.find('div',{'class':'section_strategy'}).find_all('li')
# strlist=[]
# str_news=['A. 네이버 증권 주요뉴스']

# for i in range(len(news)):
#     tmp=''
#     title = news[i].a.get_text()
#     link = 'https://finance.naver.com/' + news[i].a['href']
#     print('{}.'.format(i+1))
#     print('뉴스 제목 : ', title)
#     print('뉴스 링크 :', link)    
#     tmp='{}. {}({}) '.format(i+1,title,link)
#     str_news.append(tmp)
    
# strlist.append(str_news)
# closeBrowser(browser)



# # 날씨 정보 
# browser, soup = searchNaverByInsertTxt('날씨')
# week_weather = soup.find('ul',{'class':'week_list'}).find_all('li')

# str_weather=['C. 네이버 날씨']
# for i in range(0,2):
#     strtmp = ''

#     today_day = week_weather[i].find('strong',{'class':'day'}).get_text()
#     today_date = week_weather[i].find('span',{'class':'date'}).get_text()
#     today_weather = week_weather[i].find_all('span',{'class':'weather_inner'})
#     today_morning = today_weather[0].i.get_text()
#     today_afternoon = today_weather[1].i.get_text()
#     today_lowtemp = week_weather[i].find('span',{'class':'lowest'}).get_text()
#     today_hightemp = week_weather[i].find('span',{'class':'highest'}).get_text()


#     print(today_day, today_date)
#     print('오전: {}, 오후: {}'.format(today_morning,today_afternoon))
#     print(today_lowtemp,today_hightemp)
    
#     strtmp='{}({})의 오전: {}, 오후: {}, 최저기온: {}, 최고기온: {}'.format(today_day,today_date,today_morning,today_afternoon,today_lowtemp,today_hightemp)
#     str_weather.append(strtmp)
# strlist.append(str_weather)
# closeBrowser(browser)



# # csv 저장 
# f, writer = openCSV('test.csv')


# # print(caracciendts[0])
# title = "년도	2016년	2017년	2018년	2019년	2020년"
# title = title.split('\t')
# writer.writerow(title)

# closeFile(f)

# # image 저장 
# browser, soup = searchNaverWithlinkText('책')
# # browser.get_screenshot_as_file('screenshot.jpg')

# img_url=soup.find('a',{'id':'fist_thisBestseller_img'}).img['src']
# f = saveImg('bestsellerbook.jpg',img_url)
# closeFile(f)
# closeBrowser(browser)


# sendEmail('rimicom@naver.com','안녕','이건테스타야')

# sendEmailWithAttachment('rimicom@naver.com','안녕','이건테스타야','멜론100.csv')