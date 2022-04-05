# def fun1(v1,v2):
#     def fun2(num1,num2):
#         return num1+num2
#     return fun2(v1,v2)

# print(fun1(10,20))
# # fun2(10,20) -> error 내부함수는 호출 할 수 없다 

# def hap(n1,n2):
#     result = n1+n2
#     return result

# print(hap(1,2))

# # 함수를 한줄로 만들어주는 것이 람다함수
# hap2 = lambda n1,n2:print(n1+n2)
# hap2(11,hap(1,2))
# # hap2(10,lambda n1,n2:print(n1+n2))

# print(hap(11,hap(1,2)))

# 1부터 100까지 더하기 함수를 만들어서 출력하시오

def sumsum(n1,n2):
    sum = 0
    if n1>n2:
        n1,n2 = n2,n1
    for i in range(n1,n2+1):
        sum+=i
    return sum

# print(sumsum(1,100))



# 입력한 값에 더하기 10을 해주는 함수를 만들고 람다식도 만들기

def plus10(n):
    return n+10

pl10 = lambda n: n+10
# print(pl10(10))
# print((lambda n1,n2:n1+n2)(10,20))

# # num=int(input('숫자를 입력하세요 >> '))
# num=7
# print(plus10(num))
# print(pl10(num))

list1 = [1,2,3,4,5]
for i in range(len(list1)):
    list1[i]=(lambda n: n+10)(list1[i])
print(list1)