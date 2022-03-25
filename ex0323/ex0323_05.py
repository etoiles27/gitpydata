# import time

# print('프로그램 시작')
# print('cat 은 무슨 뜻일까요 ?')
# time.sleep(5)
# print('고양이 입니다.')

from urllib import request

rs = request.urlopen('http://naver.com')
print(rs.read())