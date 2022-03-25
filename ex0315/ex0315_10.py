from random import *
# aa = [1,2,3,4,5]

# u_num = 0
# while True:
#     u_num = int(input("1-5 중 원하는 숫자를 입력하세요 >> (종료 : 9)"))

#     for i, a in enumerate(aa):
#         if u_num == a:
#             aa[i] = 'X'

#     print(aa)
#     if u_num ==9:
#         break

# [1,...,25] 까지의 배열을 만든다. 
randNum = [i+1 for i in range(25)]
print(randNum)


# 배열을 섞고자 한다. 
for i in range(500):
    rnum = randint(0,24)
    randNum[0],randNum[rnum] = randNum[rnum],randNum[0]
    
print(randNum)
