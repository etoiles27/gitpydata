import requests

# res=requests.get("http://www.naver.com")
res=requests.get("https://www.melon.com/")

res.raise_for_status() # 코드 200가 아니면 프로그램을 자동종료 

# res.status_code : 200 정상코드, 403 권한없음, 404 페이지없음  , 50x 프로그램오류..... 
if res.status_code == requests.codes.ok: # if res.status_code == 200:
    print("정상적으로 페이지가 열립니다.")
else:
    print("페이지가 문제가 있습니다.")


print(res.text)