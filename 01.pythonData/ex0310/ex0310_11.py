

# 동전 교환 프로그램 

money, c500, c100, c50, c10 = 0,0,0,0,0

money = int(input('교환할 돈을 입력하세요 : '))
print('입력한 금액 : ', money)

c500 = money//500 
money %= 500

c100 = money//100
money %= 100

c50 = money//50
money %= 50

c10 = money//10

print('500원 {} 개 \t100원 {} 개 \t50원 {}개 \t10원 {}개'.format(c500,c100,c50,c10))