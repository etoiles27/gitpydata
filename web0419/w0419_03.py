from email import header
import imp


import requests

headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
# res=requests.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
res=requests.get("http://www.melon.com", headers=headers)
res.raise_for_status()

# print(res.text)


with open("melon.html","w",encoding="utf-8") as f:
    f.write(res.text)