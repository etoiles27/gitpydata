from random import *

# 1-100 사이에 있는 랜덤숫자 생성 
temp = randint(1,100)

# while True:
#     input1 = int(input('1 - 100 사이의 숫자를 입력하세요 : '))
#     if temp == input1:
#         print("정답입니다! 정답숫자는 {} 입니다.".format(input1))
#         break
#     elif temp >= input1:
#         print("입력하신 숫자 {} 가 작습니다. 더 큰 수를 입력하세요".format(input1))
#     else:
#         print("입력하신 숫자 {} 가 큽니다. 더 작은 수를 입력하세요".format(input1))
        

# 10 회 도전 이후에 끝 
cnt = 0
input_list = []
tN = 5
while cnt<tN:
    input1 = int(input('1 - 100 사이의 숫자를 입력하세요 : '))
    input_list.append(input1)
    cnt += 1
    if temp == input1:
        print("정답입니다! 정답숫자는 {} 입니다.".format(input1))
        break
    elif temp >= input1:
        print("입력하신 숫자 {} 가 작습니다. 더 큰 수를 입력하세요".format(input1))
    else:
        print("입력하신 숫자 {} 가 큽니다. 더 작은 수를 입력하세요".format(input1))
if cnt == tN:
    print("{}번의 입력을 초과하셧습니다. 정답숫자는 {}입니다. ".format(tN,temp))   


print('총 입력하신 숫자들은 {} 입니다'.format(input_list)) 

#input_list.sort() # 순차정렬
input_list.sort(reverse=True) # 역순정렬
print(input_list)    