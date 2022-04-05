# # 두 수를 입력받아 사칙연산이 되도록 프로그램하시요. 
# # 무한반복. 
# # 2번까지 실행 
# # 입력한 값을 출력

# cnt = 0
# input1_list =[]
# input2_list =[]

# while True:
#     if cnt < 2:
#         input1 = int(input("첫번째 숫자를 입력하세요:  "))
#         input2 = int(input("두번째 숫자를 입력하세요:  "))
#         input1_list.append(input1)
#         input2_list.append(input2)
#     else:
#         break
#     cnt += 1


# for i in range(len(input1_list)):
#     print('{} + {} = {}'.format(input1_list[i],input2_list[i],input1_list[i]+input2_list[i]))
#     print('{} - {} = {}'.format(input1_list[i],input2_list[i],input1_list[i]-input2_list[i]))
#     print('{} * {} = {}'.format(input1_list[i],input2_list[i],input1_list[i]*input2_list[i]))
#     print('{} / {} = {}'.format(input1_list[i],input2_list[i],input1_list[i]/input2_list[i]))


list1 = [[0,0],[0,0]]

# 깊은 복사 ( 새로운 공간을 만들어서 생성)
list2 =[[0]*2 for _ in range(5)]
list3 = [[0]*2]*5 # 동일한 공간을 사용. 주소값 동일. 

print(list1)
print(list2)
print(list3)


t_num = 0
while True:
    if t_num <len(list2):
        
        input1 = int(input("첫번째 숫자를 입력하세요:  "))
        input2 = int(input("두번째 숫자를 입력하세요:  "))
        
        list2[t_num][0] = input1
        list2[t_num][1] = input2

    else:
        break
    t_num += 1

print(list2)