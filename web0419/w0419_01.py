import requests

# url 모든 정보를 가져온다
res = requests.get("http://www.google.com")

# res.txt --> 문자 출력
print(len(res.text))
# print(res.text)

# 파일저장
with open("mygoogle.html","w",encoding="utf-8") as f:
    f.write(res.text)