import csv
import requests


def openCSV(fn):
    filename=fn
    f=open(filename, 'w',encoding='utf-8-sig',newline='')
    writer = csv.writer(f)
    return f, writer

    
def closeFile(f):
    f.close()

def saveImg(fn,img_url):
    headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    img_res = requests.get(img_url)
    res = requests.get(img_url,headers=headers)
    res.raise_for_status() 
    with open(fn,"wb") as f:
        f.write(img_res.content)
    
    return f


