from lottoFunc import * 

lotto6=[]
userInput=[]
lottoNum(lotto6)
user6numInput(userInput)
mlist = lottoMatch(lotto6,userInput)

print(' 로또 넘버 : {}'.format(lotto6))
print(' 입력 넘버 : {}'.format(userInput))
print(' 당첨 숫자: {} \n 당첨 넘버 : {}'.format(len(mlist),mlist))