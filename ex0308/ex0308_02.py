
# 문자열을 사용하여 프린트로 출력하기
str1 = "name"
print("이름을 영어로 하면 무엇일까요? ", str1)

# 프린트 시 문자열을 중간에 삽입하는 방법
str2 = "jane"
print("나의 이름은 %s 입니다" %str2)

# 정수 계산 시 print 내에 사칙연산 가능 
num1 = 10
num2 = 100
num3 = 1000
print("%d + %d + %d = %d"%(num1,num2,num3,num1+num2+num3))

# 실수타입이 있을 때
num4 = 10
num5 = 100.3
num6 = 1000
print("%d + %f + %d = %f"%(num4,num5,num6,num4+num5+num6))
print("%d + %.1f + %d = %.2f"%(num4,num5,num6,num4+num5+num6)) 
# %.1f 나 %.2f를 통해 표시되는 자릿수를 정할 수 있다

print("-"*10)
print("{}+{}+{}={}".format(num4,num5,num6,num4+num5+num6))
# format 함수를 사용하면 손쉽게 입력할 수 있다. 
# 문자열%s가 가장 크다 %s > %f > %d

print("*"*10)
print("100")
print("%d"%100)

print("100+100")
print("%d"%(100+100))

print("%d %d"%(100,200))
