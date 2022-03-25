# for문 

# for 문 안에 range도 올 수 있고 list 도 올 수 있다. 
# 순차적으로 출력하고 싶을때 range를 사용하면 된다 

for num in range(0,10):
    print(num)


fruits = ['사과','복숭아','딸기','배','포도','수박']
for fruits in fruits:
    print(fruits)
    
    
# list에 저장하고 싶을 때 
aa=[]
for num in range(0,10):
    print(num)
    aa.append(num)

print(aa)
