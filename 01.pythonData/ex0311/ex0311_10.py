
# list에 1~45까지의 숫자를 넣기

from random import *

# lis1 =[i for i in range(1,46)]
# lis2 = []
# for i in range(0,45):
#     lis2.append(i+1)
    
# print(lis2)

numbers =[i for i in range(1,46)]
# ran_num = randint(0,44)
# numbers[],numbers[ran_num] = numbers[ran_num],numbers[]

# cnt = 0
# for i in range(0,501):
#     # 랜덤숫자
#     ran_num = randint(0,44)
#     if cnt<44:
#         cnt += 1
#         numbers[cnt],numbers[ran_num] = numbers[ran_num],numbers[cnt]
#     else:
#         cnt = 0



for i in range(500):
     ran_num = randint(0,44)
     numbers[0],numbers[ran_num] = numbers[ran_num],numbers[0]
    
    
print(numbers)