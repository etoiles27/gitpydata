
# 두 수를 입력받아 작은수부터 출력하세요
# 10, 5 를 입력받으면 -> 5, 10 

# list1 = []
# n1 = int(input('첫번째 숫자를 입력하세요 >> '))
# list1.append(n1)
# n2 = int(input('두번째 숫자를 입력하세요 >> '))
# list1.append(n2)
# # print(min(n1,n2),max(n1,n2))

# # if n1<n2:
# #     print(n1,', ',n2)
# # else:
# #     print(n2,', ',n1)

# # 5개를 입력받아 순차적으로 출력하세요
# n3 = int(input('세번째 숫자를 입력하세요 >> '))
# list1.append(n3)
# n4 = int(input('네번째 숫자를 입력하세요 >> '))
# list1.append(n4)
# n5 = int(input('다섯번째 숫자를 입력하세요 >> '))
# list1.append(n5)

# list1.sort()

# print(list1)

# list2=[]
# for i in range(5):
#     list2.append(int(input('{}번째 숫자를 입력하세요 >> '.format(i+1))))
    
# list2.sort()
# print(list2)

# # 제일 큰 수를 찾아내시오 -> 3개의 숫자중 
# # min(), max()함수 
# print(max(10,max(7,3)))
# # 절대값
# print(abs(-6))
# # 제곱근
# print(pow(4,2)) 
# # 반올림
# print(round(4.51))

from math import *
# # 버림
# print(floor(12.9))
# # 올림
# print(ceil(14.1))


# 10.275 올림
a = 10.275
# 10.28 만들기 
b = round(a,2)
print(b)
print("{:.2f}".format(a))