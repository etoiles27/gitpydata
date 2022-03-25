# import lotto # 함수호출
from lotto import *

lottoNum=[]
lotto6=[]
lottoInput=[]
lottoM=[]

# 모듈화
# lotto.lottoProduce(lottoNum) # 로또 번호생성 함수
# lotto.lottoSuffle(lottoNum,lotto6) # 로또 번호 섞기
# lotto.inputNum(lottoInput) # 번호입력
# lotto.lottoMatch(lotto6,lottoInput,lottoM) #당첨번호 확인
lottoProduce(lottoNum) # 로또 번호생성 함수
lottoSuffle(lottoNum,lotto6) # 로또 번호 섞기
inputNum(lottoInput) # 번호입력
lottoMatch(lotto6,lottoInput,lottoM) #당첨번호 확인

# 결과 출력
print('-'*50)
print('로또번호 : ',lotto6)
print('입력번호 : ',lottoInput)
print('당첨개수 : ',len(lottoM))
print('당첨번호 : ',lottoM)