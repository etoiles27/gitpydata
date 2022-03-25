from random import *
# 로또 6개 숫자 출력
lottoNums = [i+1 for i in range(45)]
lotto = []
cnt = 0
for i in range(500):
    rno = randint(0,44)
    lottoNums[0],lottoNums[rno]=lottoNums[rno],lottoNums[0]

lotto = lottoNums[:6]

# 로또번호 입력 6개 입력
u_input =[] # 입력번호 리스트
mark_lotto = [i+1 for i in range(45)] #로또에 체크하는 리스트 

for i in range(6):
    m_cnt = 0 #45까지 출력되도록 체크하는 변수 
    print('[ LOTTO CARD ]')
    print('-'*75)
    for i in range(5):
        for j in range(10):
            if m_cnt == 45:
                break

            print(mark_lotto[10*i+j],end='\t')
            m_cnt += 1
        print()
    print('-'*75)
    
    # u_in=int(input("숫자를 6개를 입력하세요 {}번째 >> ".format(i+1)))
    print("숫자 6개를 입력하세요. {}번째 숫자입니다.".format(i+1))
    u_in=int(input("입력하신 숫자는 {} 입니다. >> ".format(u_input)))
    u_input.append(u_in)
    mark_lotto[u_in-1]='X'


print("입력번호 : {}".format(u_input))
    
# 로또 당첨 번호 생성 (6개 숫자 출력)
lottoNums = [i+1 for i in range(45)]
lotto = [] # 로또 당첨번호 리스트
cnt = 0
for i in range(500):
    rno = randint(0,44)
    lottoNums[0],lottoNums[rno]=lottoNums[rno],lottoNums[0]

lotto = lottoNums[:6]
print("로또번호 : {}".format(lotto)) 



# 사용자 입력과, 로또 번호 비교 
# 당첨확인
in_lotto = [] # 당첨된 변호 리스트
mat_count = 0 # 당첨금액 출력 

for num in u_input: #enumerate : 인덱스번호와 데이터 값이 넘어온다. 
    if num in lotto:
        in_lotto.append(num)
        #mat_count += 1
        
mat_count = len(in_lotto)
    
print("당첨번호 : {}\n당첨개수: {}".format(in_lotto,mat_count))     




reward = ["꽝","1000원","500만원","5000만원","1억원","50억원","100억원"]
print('당첨금액 : {}'.format(reward[mat_count]))
#print('당첨금액 : {}'.format(reward[mat_count%6]))