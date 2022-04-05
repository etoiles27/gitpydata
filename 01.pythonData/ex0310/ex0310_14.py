
# input1 = int(input("enther number : "))

# if input1>100:
#     print("bigger than 100")
# else:
#     print("smaller than 100")

from pickle import TRUE
from random import *

# random 함수를 사용하기 위해 불러온다. 

num = randint(1,45) # 1과 45 사이의 숫자를 랜덤으로 배정한다
count = 1

while True:
    print('*'*20)
    input1 = int(input("enter number : "))
    print('u tried {} times'.format(count))
    if num==input1: # 조건문
        print("same number ! \ninput number is {} \nrandom number is {}".format(input1,num))
        break   # while 문 종료
    else:
        print("not the same number \tinput number is {}".format(input1))
        if count == 5:
            print('-'*20)
            print('u tried 5 times \trandom number is {}'.format(num))
            print('-'*20)
            break # while 문 종료
        count += 1 # 1 증가 
