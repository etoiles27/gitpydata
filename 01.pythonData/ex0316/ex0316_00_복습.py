from random import *

# [1,2...,25] 배열을 만든다. 
randArr= [i for i in range(1,26)]
print(randArr)

# 배열을 랜덤하게 섞는다
for i in range(500):
    r_num =  randint(0,24)
    randArr[0],randArr[r_num]=randArr[r_num],randArr[0]
print(randArr)

# 배열을 5개로 끝어 2차배열로 저장한다 
randList = []
for i in range(5):
    r = [randArr[i*5+j] for j in range(5)]
    randList.append(r)
print(randList)
# 1-25 사이의 값을 입력 받아.
# 입력받은 값을 'X'와 치환 하는 무한루프
u_in = 0
while True:
    u_in = int(input('1-25까지의 숫자중 한개를 입력하세요  (종료: 100 입력) >> '))
    for idx, arr in enumerate(randList):
        if u_in in arr:
            randList[idx][arr.index(u_in)] = 'X'
    # 출력
    print(randList)
    if u_in == 100:
        break