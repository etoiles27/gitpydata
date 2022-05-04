#import random
# temp = random.random()
# print(temp)
# # 소수점 3째자리에서 반올림 
# print(round(temp,2))
# print(round(temp*100)/100)

from random import *

numList=[i for i in range(1,46)]
print(numList)
# 파괴함수 -> 원본을 손상시킴 
shuffle(numList) # 리스트 섞기 가능한 함수

print(numList)

print(sample(numList,5)) # 리스트안에서 5개를 뽑는다 