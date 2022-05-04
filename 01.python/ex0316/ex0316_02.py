# aa = [
#     [1,2,3,4],
#     [5,6],
#     [7,8,9]
# ]

# for a2 in aa:
#     for a in a2:
#         print(a)

# stu = [1,'홍길동',100,100,200,100.0,0]
# aa = {'no':1, 'name':'홍길동', 'kor':100, 'eng':100, 'total':200, 'avg':100.0, 'rank':0  }

# print(aa['total'])

stu1 = {'stu_no':1,'name':'홍길동','major':'컴퓨터공학과'}
print(stu1['major'])

# 추가하는 방법 
stu1['tel'] = '010-0000-0000'
print(stu1)
# 삭제하는 방법
del(stu1['tel'])
print(stu1)

print(stu1.get('tel')) # none 으로 출력된다. 
#print(stu1['tel']) # 없는 키값 출력으로 error

print(stu1.keys())
print(stu1.values())

li1 = list(stu1.keys())
print(li1)

print(stu1.items()) # 튜플

print('name' in stu1) # true, false 로 나타난다. 

if 'name' in stu1:
    print('name 키가 잇습니다')
else:
    print('name 키가 없습니다')