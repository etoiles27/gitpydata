from random import *

# 랜덤넘버 추출 
# 1-45까지의 리스트를 만든다. 
numlist = [i for i in range(1,46)]
userInput = [] # 사용자로부터 입력받는 6개 숫자로 이루어진 리스트 
# numlist를 랜덤하게 셔플한다. 
for i in range(500):
    n = randint(0,44)
    numlist[0],numlist[n]=numlist[n],numlist[0]

#랜덤으로 섞인 numlist에서 숫자 6개 추출
lotto6 = numlist[:6]

# 사용자로부터 6개의 숫자를 입력받음
for i in range(6):
    un = int(input('{}번째 숫자를 입력하세요 >> '.format(i+1)))
    userInput.append(un)

print(' 로또 넘버 : {}'.format(lotto6))
print(' 입력 넘버 : {}'.format(userInput))

# 매치하는지 카운트.
mCnt = 0 
mlist =[]
for i in lotto6:
    if i in userInput:
        mCnt+=1
        mlist.append(i)

print(' 당첨 숫자: {} \n당첨 넘버 : {}'.format(mCnt,mlist))