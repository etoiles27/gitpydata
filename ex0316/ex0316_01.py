
from random import * # 랜덤에 있는 모든 함수를 import 시킨다. 
# import random # 일 경우에는 random.randint() 로 사용해야한다. 

# 1. 리스트 생성 
# 2. 리스트에 1-25 까지의 숫자입력
randNum = [ i for i in range(1,26)]

# print(randNum)

# 3. 리스트 랜덤섞기
for i in range(200):
    # 랜덤숫자 생성
    rno = randint(0,24) # randint(a,b) a부터 b까지의 숫자. randrange(a,b)-> a부터 b-1 까지 숫자 
    # 숫자를 서로 자리변경 
    randNum[0],randNum[rno] = randNum[rno],randNum[0]

# print(randNum)

# 4. 2차원 배열 리스트생성
arrs = []

# 5. 1차원 리스트를 2차원 리스트에 추가
for i in range(5):
    a = [randNum[i*5+j] for j in range(5)]
    arrs.append(a)
# print(arrs)

# 6. 2차원 리스트 출력 
for arr in arrs:
    for a in arr:
        print('{}'.format(a),end='\t')
    print()

# 7. 무한루프 -> 원하는 숫자를 입력받음 
input1 = 100
while True:
    input1= int(input('원하는 번호를 입력하세요 (종료 0) >> '))
    # 8. 입력된 숫자를 'X' 로 변경 
    for idx ,arr in enumerate(arrs):
        if input1 in arr:
            arrs[idx][arr.index(input1)]='X'
            
    for arr in arrs:
        for a in arr:
            print('{}'.format(a),end='\t')
        print()
    print('-'*40)
    
    if input1 == 0:
        break
