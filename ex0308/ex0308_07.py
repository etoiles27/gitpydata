# 3개의 숫자를 입력받아 
# *** +++ --- /// (나누기는 실수형으로 출력하세요)


a = int(input('첫번째 숫자를 입력하세요: '))
b = int(input('두번째 숫자를 입력하세요: '))
c = int(input('세번째 숫자를 입력하세요: '))


print("{} + {} + {} = {}".format(a,b,c,a+b+c))
print("{} - {} - {} = {}".format(a,b,c,a-b-c))
print("{} * {} * {} = {}".format(a,b,c,a*b*c))
print("{} / {} / {} = {}".format(a,b,c,float(a/b/c)))
print("{0:f} / {1:f} / {2:f} = {3:f}".format(a,b,c,(a/b/c)))

# type 알아보는 방법 

num1 = 10.3
print(type(num1)) # float

num2 = 5
print(type(num2))  #int

str1 = "hello world"
print(type(str1)) #string

var1 = 100
var1 = var1+200 # var1 += 200 과 같다. 

# 마찬가지로 나머지 사칙연산도 var1 *= 200, var1 -= 200, var1 /= 200 으로 표기할 수 있다. 

print('var1:', var1)