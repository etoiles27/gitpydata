# # 변수
# # 선언 , 변경 쉬움 
# a =1
# print(a)
# a = 3
# print(a)

# # 리스트 , 수정, 삭제 변경 가능
# list1=[1,2,3,4,5,{1:'aaa'},[9,8,7]]
# list1[3]=6
# list1.append(7)
# print(list1)
# del(list1[3])
# print(list1)

# # 튜플은 리스트와 동일하나 변경/삭제 불가 (추가도 안됨)
# dtuple = (1,2,3,4,5,{1:'aaa'},[9,8,7])
# print(dtuple[0])

# # 딕셔너리
# datadic={1:'aaa',2:'bbb','id':'kkk'}
# print(datadic)
# datadic[1] = 'ddd' # 변경
# print(datadic)
# datadic['pw'] = '1111' # 추가
# print(datadic)
# del(datadic[1]) # 삭제 
# print(datadic)


# studic={'stuno':1,'stuname':'홍길동','kor':100,'eng':100,'total':(100+100),'avg':(100+100)/2,'rank':0}

# print(studic.items())
# for k,v in studic.items():
#     print('{} : {}'.format(k,v), end='\t')
    
studic={'stuno':1,'stuname':'홍길동','kor':100,'eng':100,'total':(100+100),'avg':(100+100)/2,'rank':0}
stulist=[{'stuno':1,'stuname':'홍길동','kor':100,'eng':100,'total':(100+100),'avg':(100+100)/2,'rank':0},\
         {'stuno':2,'stuname':'이순신','kor':99,'eng':100,'total':(99+100),'avg':(99+100)/2,'rank':0},\
         {'stuno':3,'stuname':'유관순','kor':99,'eng':99,'total':(99+99),'avg':(99+99)/2,'rank':0}]


while True:
    print(stulist)
    search_name = input('찾고자하는 이름을 입력하세요 >> ')
    count = 0
    for i, stu in enumerate(stulist):
        if search_name in stu.values(): #== stu['stunamegh']:
            print('{}이 있습니다.'.format(search_name))
            del(stulist[i])
            print('{}이 삭제되었습니다.'.format(search_name))
            count += 1
            break

    if count == 0:
        print('{}이 없습니다.'.format(search_name))