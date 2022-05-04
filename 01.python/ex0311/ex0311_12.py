# # 0-100 7의 배수의 합을 구하시오 
# sum = 0 
# lis7=[]
# for i in range(0,100,7):
#     sum += i
#     lis7.append(i)
# print(lis7)
# print('7의 배수의 합: ', sum)


# # 0 -100 홀수의 합을 구하시오
# odd_sum = 0
# lis_odd=[]
# for i in range (1,100,2):
#     odd_sum += i
#     lis_odd.append(i)
# print(lis_odd)
# print('홀수의 합: ', odd_sum)



# sum7 = 0
# lis=[]
# for i in range(1,100):
#     if i%7 == 0:
#         sum7 += i
#         lis.append(i)

# print(sum7)
# print(lis)



# sumO = 0
# lisO=[]
# for i in range(1,100):
#     if i%2 == 1:
#         sumO += i
#         lisO.append(i)

# print(sumO)
# print(lisO)


# 두 수를 입력받아 홀수의 값의 합을 출력하시오 
# 1, 10 -> 홀수 의 합
num1 = int(input('첫번째 수를 입력하세요 : '))
num2 = int(input('두번째 수를 입력하세요 : '))

if num1>num2:
    num1, num2 = num2, num1

odd_sum = 0
odd_lis = []
for i in range(num1, num2+1):
    if i%2 == 1:
        odd_sum += i 
        odd_lis.append(i)

print('홀수 총합은 {} \n홀수는 {}'.format(odd_sum,odd_lis))