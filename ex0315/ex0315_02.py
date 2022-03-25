# # 구구단 출력

# for i in range(2,10):
#     print('{} 단'.format(i))
#     for j in range(1,10):
#         print("{} * {} = {} ".format(i,j,i*j),end='  ')
#     print()
    
# print('-'*70)

# print('2단 \t\t3단 \t\t4단 \t\t5단 \t\t6단 \t\t7단')
# for i in range(1,10):
#     for j in range(2,8):
#         print("{} * {} = {} ".format(j,i,i*j),end='\t')
#     print()


# list1 = ['주바다','공유진','김샛별','송선유','양홍욱']
# for i, val in enumerate(list1):
#     print('{}. {}'.format(i+1,val))

# print('-'*20)
# idx = 1 
# for k in list1:
#     print('{}. {}'.format(idx,k))
#     idx += 1
# print('-'*20)

# for nm in range(len(list1)):
#     print('{}. {}'.format(nm+1,list1[nm]))

# # 한줄 for 문
# list1 = [i for i in range(10)]
# print(list1)
# print(type(list1))
# print(type(list1[0]))


list1 = ['주바다','공유진','김샛별','송선유','양홍욱','윤상훈','이한구']

while True:
    search = input('이름을 입력하세요 >>')
    if search in list1:
        print(' 출석! ')
    else:
        print(' 출석 전 ')