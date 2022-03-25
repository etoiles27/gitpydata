# 비밀번호를 naver+글자총길이수+c가들어간개수+!!를 넣어서 출력
# => naver201!!
# 비밀번호생성프로그램
url = 'http://www.naver.com'

#replave 사용
ns=url.replace('http://www.','')
# .com 은 index or find 사용
n=ns.find('.')

pwd = ns[0:n]+str(len(url))+str(url.count('c'))+'!!'

print(pwd)


