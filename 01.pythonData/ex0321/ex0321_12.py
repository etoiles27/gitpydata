# lotto 맞추기 게임을 만든다. 
# lotto 6 생성
# 입력 6 생성
# 로또번호 입력번호 확인
# 똑같은 로또번호 개수 번호를 출력하시오 

from random import*
import test 

# def lottoNum():
#     lottoN=[i for i in range(1,46)]




lottoN=[]
test.lottoNum(lottoN)

print(lottoN)
# 6개 랜덤 로또 넘버 생성
for i in range(500):
    num = randint(0,44)
    lottoN[0],lottoN[num]=lottoN[num],lottoN[0]

lotto = lottoN[:6]

# 6개의 사용자 입력
u_in = []
for i in range(6):
    n = int(input("숫자 6개를 입력하세요 {}번째 숫자입니다 >> ".format(i+1)))
    u_in.append(n)


print('로또번호: {} \n사용자 입력: {}'.format(lotto,u_in))    

# 매치넘버, 세기
m_cnt = 0
mat = [] 
for i in lotto:
    if i in u_in:
        mat.append(i)
        m_cnt +=1
    
print("매치 넘버는 {}개 번호는 : {}".format(m_cnt,mat))