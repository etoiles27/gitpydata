# list 

# 변수 
a = 1 
b = 2 
c = 3
d = 4
e = 5 

# list -> 같은 이름으로 변수 5개를 선언한 것과 같다. 
bb = [1,2,3,4,5]

bb[0] # 1 을 의미한다. 

aa = [0,0,0,0,0]

aa[0] = 1
aa[1] = 2
aa[2] = 3
aa[3] = 4
aa[4] = 5

# list에 추가하기 위해서는 append를 사용한다. 

print(aa)
aa.append(6)
print(aa)

# list안에 list를 넣을 수 도 있고 타입이 다른 문자도 넣을 수 있다. 

cc = [i for i in range(0,25)]  # list 안에 for문을 넣을 수 있다. 
print(cc)

if 1 in cc:
    print('1이 존재합니다')
else:
    print('1이 존재하지 않습니다. ')
    

fruit = ['사과','복숭아','딸기','배','포도','수박']

if '딸기' in fruit:
    print('딸기가 있습니다.')
    
fruit.append('한라봉')

print(fruit)