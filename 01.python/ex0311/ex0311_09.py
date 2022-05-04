# 숫자 두개를 입력받아 

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))

# num1부터 num2 사이의 숫자를 더하시오 

# num2 가 num1보다 작은 숫자가 입력되었을경우
# 둘을 치환해 준다. 

if num1>num2:
    num1,num2 = num2,num1 # python에 있는 두개의 변수 바꾸는 방법. 


sum = 0
for i in range(num1,num2+1):
    sum += i

print('총 합 : ',sum)

# # eval()함수는 문자를 숫자로 변경해주는 함수 
# num3 = input('세번째 숫자를 입력하세요 : ')
# num3 = eval(num3)
# print(num3+1)