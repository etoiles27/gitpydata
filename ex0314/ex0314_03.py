
# # 1- 100 홀수만 출력

# ch = 0 
# while ch<=100:
#     if ch%2==1:
#         print('{}'.format(ch))
#     ch +=1
    
# 구구단 출력

# ck = 1
# while ck < 10:
#     if ck%3 != 0 :
#         print('2 * {} = {}'.format( ck , 2*ck))
#     ck += 1 

# continue 
# 밑에를 실행시키지 않고 다시 위로 올라간다.(한번만 빠져나옴)
# break 와 다른점은 break는 완전히 빠져나옴.
ck = 1
while ck < 10:
    if ck%3 == 0 :
        ck += 1
        continue
    print('2 * {} = {}'.format( ck , 2*ck))
    ck += 1 
    