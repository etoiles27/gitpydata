
# # list 0-100 들어가는 list를 for 문으로 출력하세요 

# ls1 = [i for i in range(0,101)]  # 한줄 for문
# print(ls1)

# ls2 = []
# for num in range(0,101):
#     ls2.append(num)
# print(ls2)


# 0 - 100 짝수만 넣기 
ls3 = []
for num in range(0,101):
    if num%2 == 0:
        ls3.append(num)
print(ls3)

