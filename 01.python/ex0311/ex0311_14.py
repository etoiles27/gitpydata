

# for i in range(2,10):
#     print('[ {} ] 단'.format(i))
#     for j in range(1,10):
#         print('{} * {} = {}  '.format(i,j,i*j),end='')
#     print()
    
    
# for i in range(1,10):
#     for j in range(2,10):
#         print('{} * {} =  {}\t'.format(j,i,i*j),end='')
#     print()
   
# # 입력한 단 부터 9 단까지 출력하기

# num = int(input('숫자를 입력하세요 : '))

# for i in range(1,10):
#     for j in range(num,10):
#         print('{} * {} = {}\t'.format(j,i,i*j),end = '')
#     print()


# 입력한 단 부터 입력한 단까지 출력하기

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))

if num1>num2:
    num1,num2 = num2,num1

for i in range(1,10):
    for j in range(num1,num2+1):
        print('{} * {} = {}\t'.format(j,i,i*j),end = '')
    print()
