
from random import *

# 1-45 까지의 로또 번호 생성
def lottoProduce(lottoNum):
    for i in range(45):
        lottoNum.append(i+1)
        
# 로또 번호 랜덤하게 섞고 6개의 로또 번호 추출    
def lottoSuffle(lottoNum,lotto6):
    for i in range(500):
        rnum = randint(0,44)
        lottoNum[0],lottoNum[rnum]=lottoNum[rnum],lottoNum[0]
    for i in range(6):
        lotto6.append(lottoNum[i])

# 사용자 로또 번호 입력
def inputNum(lottoInput):
    num =0
    for i in range(6):
        num = int(input("6개의 숫자를 입력하세요({}번째)>> ".format(i+1)))
        lottoInput.append(num)

def lottoMatch(lotto6,lottoInput,lottoM):
    for i in lotto6:
        if i in lottoInput:
            lottoM.append(i)
            
    