# 직접입력
alist = [0,1,2,3,4,5,6,7,8,9]
# 한줄for문을 이용한 입력
blist = [ i for i in range(10)]
# 기본 for문을 통한 입력
clist = []
for i in range(0,10):
    clist.append(i)
print(alist)
print(blist)
print(clist)

# 기본 for문 으로 3의 배수 입력 (1-20)
dlist = []
for i in range(1,20):
    if i%3==0:
        dlist.append(i)
# 한줄 for문 으로 3의 배수 입력 (1-20)
elist=[i for i in range(1,20) if i%3 == 0]

print(dlist)
print(elist)



foods = ['떡볶이','짜장면','라면','피자','맥주']
sides = ['오뎅','단무지','김치','피클','땅콩']

for food, side in zip(foods,sides):
    print('{} : {} '.format(food,side))

# n = 0
# if  len(foods) < len(sides):
#     n = len(foods)
# else:
#     n = len(sides) 

# min , max 함수를 사용 할 수 있다. 
n = min(len(foods),len(sides))

for i in range(n):
    print("{} : {} ".format(foods[i],sides[i]))


# zip으로 묶으면 튜플 형태로 만들 수 있다.     
tuplist = list(zip(foods,sides))
print(tuplist)
# 튜플 리스트는 딕셔너리로 바꿀 수 있다. 
diclist = dict(tuplist)
print(diclist)

# 1개의 주소값으로 2개가 동시에 사용되어짐
# foods2 = foods
# foods2[0]='gg'
# print(foods)

# 때문에 copy를 사용
foods2 = foods.copy()

# 그러나 슬라이싱을 사용하면 딥카피가 가능하다 . 
foods3 = foods[:] # [:] -> 처음부터 끝까지. = [0:-1]-> 처음부터 마지막까지 
foods3[0]='gg'
print(foods)
