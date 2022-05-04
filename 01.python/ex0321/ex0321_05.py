# def cal(n1,n2):
#     result1, result2, result3, result4 = 0,0,0,0 
#     result1 = n1+n2
#     result2 = n1-n2
#     result3 = n1*n2
#     result4 = n1/n2
#     return result1, result2, result3, result4 

# hap = cal(1.5,2)
# print(hap)
# print(cal('aa','bb'))

def calc(n1,n2,ch):
    result = 0 
    if ch == 1:
        result = n1+n2
    elif ch ==2:
        result = n1-n2
    elif ch ==3:
        result = n1*n2
    elif ch ==4:
        result = n1/n2
    
    return result

print('[ 사칙연산 프로그램 ]')
print('1.+ 2.- 3.* 4./ ')
choice = int(input('원하는 번호를 입력하세요 >> '))
num1 = int(input('숫자를 입력하세요 >> '))
num2 = int(input('숫자를 입력하세요 >> '))

print(calc(num1,num2,choice))