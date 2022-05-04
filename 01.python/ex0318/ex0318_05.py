
# 문자열에서 특정 문자 치환, 제거 
str1='서울인재개발원은 서울에 있습니다. 서울은 동아시아권입니다.'
print(str1)
print(str1.replace('서울','한국'))
print(str1.replace('서울',''))

str_num ='123,450,000'
str_n=str_num.replace(',','')
num1 = 10000
print(int(str_n)+num1)
print('{:,}'.format(int(str_n)+num1))



#문자열 공백제거

ss = '  안   녕  하세   요     '
print(ss.strip()) # 오른쪽 왼쪽 공백 제거 
print(ss.rstrip()) # 오른쪽 공백제거
print(ss.lstrip()) # 왼쪽 공백제거 
print(ss.replace(' ','')) # 모든공백다 지우기
ss = '---안----녕-하세--요---------'
print(ss.strip('-'))

in_str=input('아이디를 입력하세요')
com_str = in_str.replace(' ','')
print('아이디 :  {}'.format(com_str),end='---')


