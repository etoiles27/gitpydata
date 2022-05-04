from random import *

# print(random()) # random() 0<random()<1
# print(randint(1,45)) # 1<= n <=45

# # 1-45 로 리스트를 채우는 방법 
# list1 =[i+1 for i in range(45)]
# print(list1)
# list2 = []
# for i in range(45):
#     list2.append(i+1)

# print(list2)

# list3 = range(1,46)
# print(list(list3))

# lotto=[i+1 for i in range(45)]
# #6개의 수를 뽑아보세요 
# lottoNum=[]
# cnt=0
# while cnt<6:
#     rno = randint(0,44)
#     if not lotto[rno] in lottoNum:
#         lottoNum.append(lotto[rno])
#         cnt += 1
# print(lottoNum)

# # if 가 들어간 것 보다 속도가 빠르다. 
# lottoN = []
# for i in range(500):
#     rno = randint(0,44)
#     lotto[0],lotto[rno]=lotto[rno],lotto[0]
# lottoN = lotto[:6]
# print(lottoN)

# # python에는 셔플 함수가 있다 -> 간단하게 사용할 수 있다. 
# lotto=[i+1 for i in range(45)]

# ln = sample(lotto,6)
# print(ln)
# #shuffle(lotto)
# #print(lotto)

# 자신이 입력한 6개의 숫자와 로또 당첨 번호 6개와 비교해서 
# 몇개를 맞췃는지 출력하는 프로그램을 구현하시요
# 6개:100억 5개:50억 4개:1억 3개:5천만원 2개:500만원 1개:천원 0개:꽝
# 출력:
# 당첨번호 : 1,2,3,4,5,6
# 입력번호 : 1,2,13,14,15,16
# 당첨개수 : 1,2
# 당첨금액 : 500 만원 


# 로또 6개 숫자 출력
lottoNums = [i+1 for i in range(45)]
lotto = []
cnt = 0
for i in range(500):
    rno = randint(0,44)
    lottoNums[0],lottoNums[rno]=lottoNums[rno],lottoNums[0]

lotto = lottoNums[:6]

# 숫자 6개 입력
u_input =[]
for i in range(6):
    # u_in=int(input("숫자를 6개를 입력하세요 {}번째 >> ".format(i+1)))
    print("숫자 6개를 입력하세요. {}번째 숫자입니다.".format(i+1))
    u_in=int(input("입력하신 숫자는 {} 입니다. >> ".format(u_input)))
    u_input.append(u_in)
    
# 비교 
mat_count = 0
mat_num = []
for i in range(6):
    if lotto[i] in u_input:
        mat_count += 1
        mat_num.append(lotto[i])


# 출력 
# print("로또번호 : {}".format(lotto))    
# print("입력번호 : {}".format(u_input))
# print("당첨번호 : {}".format(mat_num)) 

print('-'*50)
print('[ 로또 결과 ]')
print("로또번호 : ",end=' ')
for i in range(len(lotto)):
    print('{:3d}'.format(lotto[i]),end=' ')

print()
print("입력번호 : ",end=' ')
for i in range(len(u_input)):
    print('{:3d}'.format(u_input[i]),end=' ')
print()
print("당첨번호 : ",end=' ')
for i in range(len(mat_num)):
    print('{:3d}'.format(mat_num[i]),end=' ')
print()    
    


ttlist = ["당첨금액 : 꽝","당첨금액 : 1000원","당첨금액 : 500만원","당첨금액 : 5000만원","당첨금액 : 1억원","당첨금액 : 50억원","당첨금액 : 100억원"]
print(ttlist[mat_count%6])

#  1-45 까지의 번호가 있고 입력한 번호는 'X' 표시되게    

# list1 = [i+1 for i in range(45)]

# for i in range(9):
#     for j in range(5):
#         if list1[i*5+j] in u_input:
#             list1[i*5+j]='X'
#         print(list1[i*5+j],end='\t')
#     print()


# for i in range(5):
#     for j in range(9):
#         if list1[i*9+j] in u_input:
#             list1[i*9+j]='X'
#         print(list1[i*9+j],end='\t')
#     print()



mark_lotto = [i+1 for i in range(45)]
m_cnt = 0
print('[ LOTTO CARD ]')
print('-'*75)
for i in range(5):
    for j in range(10):
        if m_cnt == 45:
            break
        if mark_lotto[i*10+j] in u_input:
            mark_lotto[i*10+j]='X'
        print(mark_lotto[10*i+j],end='\t')
        m_cnt += 1
    print()
print('-'*75)
    