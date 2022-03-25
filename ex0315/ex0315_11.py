from random import *

# [1,2...,25] 배열을 만든다. 
randNum = [i+1 for i in range(25)]
print('1-25숫자 배열 \n' , randNum)

# 배열을 랜덤하게 섞는다
for n in range(500):
    rnum = randint(0,24)
    randNum[0],randNum[rnum] = randNum[rnum],randNum[0] 

print('1-25 숫자배열 랜덤하게 셔플 : \n', randNum)

# 배열을 5개로 끝어 2차배열로 저장한다 
list2d = []
for i in range(5):
    arr = [randNum[i*5+j] for j in range(5)]
    list2d.append(arr)

print('랜덤한 2차 숫자 배열\n',list2d)
# 1-25 사이의 값을 입력 받아.
# 입력받은 값을 'X'와 치환 하는 무한루프

u_in = 0
while True:
    u_in = int(input("1-25 까지의 숫자를 입력하세요 [종료:100]>> "))
    
    # 치환
    for idx, arr in enumerate(list2d):
        if u_in in arr:
            list2d[idx][arr.index(u_in)]= 'X'
    # 출력
    print(list2d)
    if u_in == 100:
        break