import requests
from bs4 import BeautifulSoup
import re 
import csv

# 20-21 년 연봉.csv 파일 만들기 

for year in range(2020,2023):

    url = 'http://www.statiz.co.kr/salary.php?opt=0&sopt='+str(year)+'&te='

    headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()  
    soup = BeautifulSoup(res.text,"lxml")
    players = soup.find('table',{'class':'table table-striped'}).find_all('tr')

    filename =str(year)+'년연봉.csv'
    f=open(filename, 'w',encoding='utf-8-sig',newline='')
    writer = csv.writer(f)
    title = ['선수','연도','팀','연봉(만원)','WAR']
    writer.writerow(title)

    for i in range(len(players)):
        player_info = players[i].find_all('td')
        if player_info:
            pinfolist=[]
            p_name = player_info[0].get_text()
            p_year = player_info[1].get_text()
            p_team = player_info[2].get_text()
            p_salary = re.sub(r'[^0-9]','',player_info[3].get_text())
            p_war = player_info[4].get_text()
            pinfolist =[p_name,p_year,p_team,p_salary,p_war]
            writer.writerow(pinfolist)
            # print(pinfolist)
    f.close()
