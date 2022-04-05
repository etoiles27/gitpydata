
a = int(input('숫자를 입력하세요 :'))
b = int(input('숫자를 입력하세요 :'))

# 더하기, 빼기, 곱하기, 나누기를 출력하세요

print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)
print('-'*20)
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))

s_kor = int(input('국어점수를 입력하세요 :'))
s_eng = int(input('영어점수를 입력하세요 :'))
s_math = int(input('수학점수를 입력하세요 :'))

print('합계 : {}\n평균: {:.2f}'.format(s_kor+s_eng+s_math,(s_kor+s_eng+s_math)/3))

num1 = int(input('숫자를 입력하세요 :'))
num2 = int(input('숫자를 입력하세요 :'))
print('{}와 {}의 나누기 값 : {:.2f}'.format(num1,num2,num1/num2))
print('{}와 {}의 몫 값 : {}'.format(num1,num2,num1//num2))
print('{}와 {}의 나머지 값 : {}'.format(num1,num2,num1%num2))