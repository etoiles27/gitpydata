stu1 = {'no':1, 'name':'홍길동', 'kor':100, 'eng':100, 'total':200, 'avg':100.0, 'rank':0  }

if 'tel' in stu1:
    print(stu1['tel'])


# while True:
#     search = input('키 값을 입력하세요 >> ')
#     if search in stu1:
#         print(stu1[search])
#     else:
#         print('키값이 없습니다. 다시입력하세요 ')
#         print()

for key in stu1:  # in 의 형태에서 key 값이 넘어온다. 때문에 아래와 같이 출력이 가능하다. 
    print('{:5s} : {} '.format(key, stu1[key]))
    

print('-'*50)

i = 'kor'
if i in stu1.values():
    print(i)

print(i)