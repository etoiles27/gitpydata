import requests
from bs4 import BeautifulSoup
import csv



url = "https://www.google.com/maps/place/37%C2%B024'42.0%22N+126%C2%B054'09.6%22E/data=!3m1!4b1!4m5!3m4!1s0x0:0x6b934e96c8b42194!8m2!3d37.4116562!4d126.902678"
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")
add = soup.find("body",{"class","keynav-mode-off screen-mode"})

print(add)