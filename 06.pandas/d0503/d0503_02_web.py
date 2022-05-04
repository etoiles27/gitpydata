import requests
from bs4 import BeautifulSoup
import re 
import csv

# 1. 다음 영화 웹스크래핑
# 2016-2021 영화 5개 
# 제목, 평점, 개봉일, 누적인원
# excel 로 저장 

# 2. pandas로 변환. 
# 추천점수 컬럼을 만듦
# (관객수+평점)/100

# 3. 추천점수가 높은순으로 출력

url = 'https://search.daum.net/search?w=tot&q='+str(2016)+'%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'

headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")
movies = soup.find('ol',{'class':'type_plural list_exact movie_list'}).find_all('li')



# title = movies[0].find('div',{'class':'info_tit'}).a.get_text()
# rate = movies[0].find('em',{'class':'rate'}).get_text()
# m_info = movies[0].find_all('dl',{'class':'dl_comm'})
# m_date = m_info[1].dd.get_text().replace(' ','')
# m_count = re.sub(r'[^0-9]','',m_info[3].dd.get_text())

# m_count = re.sub(r'[^0-9]','',m_count)

# print(m_count)


filename ="daummovies.csv"
f=open(filename, 'w',encoding='utf-8-sig',newline='')
writer = csv.writer(f)
m_index=['제목', '평점', '개봉일', '누적인원']
writer.writerow(m_index)


for i in range(2016,2022):
    url = 'https://search.daum.net/search?w=tot&q='+str(i)+'%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'

    headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()  
    soup = BeautifulSoup(res.text,"lxml")
    movies = soup.find('ol',{'class':'type_plural list_exact movie_list'}).find_all('li')
    
    for j in range(5):
        tmp = []
        title = movies[j].find('div',{'class':'info_tit'}).a.get_text()
        rate = movies[j].find('em',{'class':'rate'}).get_text()
        m_info = movies[j].find_all('dl',{'class':'dl_comm'})
        m_date = m_info[1].dd.get_text().replace(' ','')
        m_count = re.sub(r'[^0-9]','',m_info[3].dd.get_text())
        tmp = [title, rate, m_date, m_count]
        
        writer.writerow(tmp)
    

f.close()