# 구구단 출력하기 

# 2 단  
for i in range(1,10):
    print('2 * {} = {}'.format(i, 2*i))
    
# 중첩 반복문 사용 

# 2 - 9단 까지 구구단 출력하기 
for i in range(2,10): 
    for j in range(1,10):
        print('{} * {} = {} '.format(i,j,j*i))
    print('-'*20)
    
# 짝수단만 출력
for i in range(2,10): 
    if i%2 == 0: 
        for j in range(1,10):
            print('{} * {} = {} '.format(i,j,j*i))
        print('-'*20)

# 구구단에서 (* 1,3,5,7,9) 만 출력 
for i in range(2,10): 
    for j in range(1,10):
        if j%2 == 1: 
            print('{} * {} = {} '.format(i,j,j*i))
    print('-'*20)