# lotto 리스트에  6개의 랜덤 숫자를 넣으세요
# 중복제거
# 숫자 6개를 입력받으세요 

import random
from random import *

# 6 개의 사용자 입력받아 userinput에 저장 
userinput = []
for i in range(0,6):
    input1 = int(input('Enter 6 number (u put {}) : '.format(i+11)))
    userinput.append(input1)
    # userinput.append(int(input('Enter 6 number (u put {}) : '.format(i))) 로 사용할 수 있다.


print(userinput)

# 중복없는 6개의 랜덤 숫자를 로또에 저장 
lotto = []
for j in range(0,6):
    j = randrange(1,46)
    if j not in lotto:
        lotto.append(j)
print(lotto)

# # whlie 구문으로 6자리 중복 없는 로또번호 만들기
# count = 0
# lotto1 = []
# while True:
#     if count <=5:
#         temp = randrange(1,46)
#         if temp not in lotto1:
#             lotto1.append(temp)
#             count += 1
#     else:
#         break

# print(lotto1)


# 사용자 입력과 로또 번호를 비교해서 몇개가 맞는지 산출

cnt=0
matched_num = []
for k in range(0,6):
    if userinput[k] in lotto:
        cnt += 1
        matched_num.append(userinput[k])
        # print('{} match num is {}'.format(cnt, userinput[k]))
    # else:
    #    print('no match')
        
print("u have [{}] matched numbers ".format(cnt))
print(matched_num)