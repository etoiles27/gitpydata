# def 함수이름(매개변수1,매개변수2...,매개변수n) => 함수호출 개수와 같아야한다.
# 매개변수 기본값설정 -> 매개변수의 기본값을 설정하면 호출개수와 달라도 호출된다.
# 기본값이 설정된 매개변수는 입력하지 않으면 기본값으로 설정된다. 
# return 개수는 상관없음. 없으면 생략 가능 . 2개이상이면 튜플타입



# 매개변수를 지정하지 않고 함수 만들기 
# 매개변수 *변수 로 설정하면, 호출개수 상관없이 함수가 호출된다. 
# *변수는 튜플로 받게된다. 


# def para_func(v1,v2,*para): # para는 가변매개변수
#     print('v1 : ',v1)
#     print('v2 : ',v2)
#     result = 0
#     print(type(para))
#     for i in para:
#         print('para : ',i)
#     return result

# para_func(1,2,3,4,5,6,7)

# # para_func 함수 생성
# # 가변 매개변수 사용
# # 매개변수 합을 리턴해서
# # 호출한 곳에서 출력하세요
# # para_func(10,20,30,40,50,60,70,80,90)

# def para_func(*para):
#     result = 0 
#     mylist = []
#     for i in para:
#         result += i
#         mylist.append(i)
#     mylist.append(result)
#     return mylist

# result = para_func(10,20,30,40,50,60,70,80,90,100)
# print('매개변수 값 : ', result[:-1])
# print('매개변수 합 : ', result[-1])



# 매개변수를 입력받아 . 출력

def para_func(para):
    result = 0 
    mylist = []
    for i in para:
        result += i
        mylist.append(i)
    mylist.append(result)
    return mylist


inputlist = []
while True:
    num = int(input('숫자를 입력하세요 (종료는 0) >> '))
    if num == 0 :
        break
    inputlist.append(num)

result = para_func(inputlist)
print('매개변수 값 : ', result[:-1])
print('매개변수 합 : ', result[-1])