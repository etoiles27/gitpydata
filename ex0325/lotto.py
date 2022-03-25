# 로또를 1-10개를 구매할 수 있다

# 로또번호에 몇개 맞앗는지 출력하세요
# 당첨금액 1등 10억 2등 1억 3등 1000만원 4등 100만원 5등 1만원 

# [1번 로또]
# 로또당첨번호 : 1,2,3,4,5,6
# 로또입력번호 : 4,5,6,7,8,9
# 당첨확인번호 : 4,5,6 (3개)
# 당청금액 : 1000만원 

# [2번 로또]
# 로또당첨번호 : 1,2,3,4,5,6
# 로또입력번호 : 6,7,8,9,10,11
# 당첨확인번호 : 6 (1개)
# 당청금액 : 0원

from random import * 

lottoNumber = [i for i in range(1,46)]
lotto6 = []
uInput = []
numuInput=[]
matnum = []
# 입력수가 10 보다 큰 경우 다시 입력받는다. 
lottocnt=0
while True:
    lottocnt = int(input("원하는 개수의 로또를 입력해주세요 (1-10) >> "))
    if lottocnt>10 :
        print('다시 입력하세요')
    else:
        break

# 로또 넘버 생성
for i in range(500):
    n = randint(0,44)
    lottoNumber[0],lottoNumber[n] = lottoNumber[n],lottoNumber[0] 

lotto6=lottoNumber[:6]

# lottocnt 만틈의 로또번호를 입력받는다. 
for k in range(lottocnt):
    print('[{}번째 로또]'.format(k+1))
    for i in range(6):
        n = int(input('6개의 숫자를 입력해주세요 {}번째 숫자 >> '.format(i+1)))
        uInput.append(n)    
    numuInput.append(uInput)
    uInput=[]

# 각각의 로또 번호를 [[],[],...] 형식으로 받는다. 


# 당첨번호와 비교 
for k in range(lottocnt):
    uInput = numuInput[k]
    for i in lotto6:
        if i in uInput:
            matnum.append(i)
        
                
    print('[{}번째 로또]'.format(k+1))            
    print('로또당첨번호 : {}'.format(lotto6))
    print('로또입력번호 : {}'.format(uInput))
    print('당첨확인번호 : {} ({}개)'.format(matnum,len(matnum)))