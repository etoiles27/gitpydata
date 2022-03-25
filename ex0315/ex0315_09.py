
from random import *
# temp = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
    
# ]

# arr1=[]
# for i in range(0,5):
#     arr2 =[5*i+j for j in range(1,6)]
#     arr1.append(arr2)

# print(arr1)

# list1= [[0]*5 for _ in range(5)]

# print(list1)

# list2 = []
# for i in range(5):
#     list3 = [0 for j in range(1,6)]
#     list2.append(list3)

# print(list2)


arrs = []
for i in range(5):
    tmp = [5*i+j for j in range(1,6)]
    arrs.append(tmp)

for arr in arrs:
    for a in arr:
        print('{:2d}'.format(a), end='   ')
    print()

# in_num = int(input("1 - 25 사이의 숫자를 입력하세요 >> "))
# # 3 이라는 숫자를 넣으면 3의 자리에 X가 입력되도록

# for i, arr in enumerate(arrs):
#     if in_num in arr:
#         arrs[i][arr.index(in_num)] = 'X'
        

# print(arrs)

# in_num = 0
# while True:

#     in_num = int(input("1 - 25 사이의 숫자를 입력하세요 >> "))
#     for i, arr in enumerate(arrs):
#         if in_num in arr:
#             arrs[i][arr.index(in_num)] = 'X'
            
#     # 출력 
#     for n in arrs:
#         for a in n:
#             print('{}'.format(a), end='\t')
#         print()
    
    
    
# [1,...,25] 까지의 배열을 만든다. 
randNum = [i+1 for i in range(25)]
print(randNum)


# 랜덤하게 배열을 섞고자 한다. 
for i in range(500):
    rnum = randint(0,24)
    randNum[0],randNum[rnum] = randNum[rnum],randNum[0]
    
print(randNum)

# 섞은 데이터를 5개씩 나누어 리스트를 만든다. 

arrs = []

for i in range(0,5):
    temp = [randNum[5*i+j] for j in range(0,5)]
    arrs.append(temp)

print(arrs)