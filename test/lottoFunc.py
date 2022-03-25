from random import *

# 랜덤넘버 추출 함수
def lottoNum(lotto6):
    # 1-45까지의 리스트를 만든다. 
    numlist = [i for i in range(1,46)]
    
    # numlist를 랜덤하게 셔플한다. 
    for i in range(500):
        n = randint(0,44)
        numlist[0],numlist[n]=numlist[n],numlist[0]
    #랜덤으로 섞인 numlist에서 숫자 6개 추출
    for i in range(6):
        lotto6.append(numlist[i])

# 사용자가 6개의 숫자를 입력하는 함수         
def user6numInput(userInput):
    for i in range(6):
        un = int(input('{}번째 숫자를 입력하세요 >> '.format(i+1)))
        userInput.append(un)

# 로또6자리와 사용자입력6자리 비교 함수 
def lottoMatch(lotto6,userInput):
    mlist =[]
    for i in lotto6:
        if i in userInput:
            mlist.append(i)

    return mlist 
    