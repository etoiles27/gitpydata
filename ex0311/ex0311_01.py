# # input함수로 입력을 받으면 string이다 
# # 숫자를 입력받고자 할때는 str-> int로 형 변환을 해야한다. 
# input1 = int(input("숫자를 입력하세요 : "))

# if input1>10:
#     print("10보다 큽니다.")
# else:
#     print("10보다 작습니다")

# input1 = int(input("숫자를 입력하세요 : "))

# # 짝수면 짝수 홀수면 홀수
# if input1%2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다")
    
# # 3의 배수 인가 아닌가
# if input1%3 == 0:
#     print("3의 배수입니다.")
# else:
#     print("3의 배수가 아닙니다.")
    
# # 비교 . 
# if 5<input1<10: # 5<input1 and input1<10
#     print("5보다 크고 10보다 작습니다")
# else:
#     print("5보다 작거나 10보다 큰 수 입니다")

# # 60점 이상이면 합격 60점 미만이면 불합격
# if input1>=60:
#     print("합격.")
# else:
#     print("불합격")

input1 = int(input("점수 를 입력하세요 : "))


# if 와 elif , 중첩 if문
if input1>=90:
    print('A', end='')
    if input1>=98:
        print('+')
    elif 93>=input1>=90:
        print('-')
elif input1>=80:
    print('B', end='')
    if input1>=88:
        print('+')
    elif 83>=input1>=80:
        print('-')     
elif input1>=70:
    print('C', end='')
    if input1>=78:
        print('+')
    elif 73>=input1>=70:
        print('-')
elif input1>=60:
    print('D',end='')
    if input1>=68:
        print('+')
    elif 63>=input1>=60:
        print('-')
else:
    print('F')

