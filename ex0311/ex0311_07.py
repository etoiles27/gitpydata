import random 
from random import *

lottonum = randrange(1,46) # range 를 쓸 경우에는 1~45
# = randint(1,45) 이것과 같다. 
print(lottonum)

# lotto 6개를 저장해서 출력하세요 . list에 저장. 
# 중복을 제거 하는 방법 생각하기 


lotto = [] # list로 저장공간 만들기 

# for i in range(0,6):
#     temp = randrange(1,46)    
#     if temp not in lotto:
#         lotto.append(temp)
    
# print(lotto) 

count = 0
while True: # 무한반복
    if count <= 5:
        temp = randrange(1,46)
        if temp not in lotto:
            lotto.append(temp)
            count += 1
    else:
        print('6개의 번호가 추출되엇습니다.')
        break

print(lotto)
