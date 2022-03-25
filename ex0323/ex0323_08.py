
try:
    input1 = int(input('숫자1를 입력하세요 >> '))
    input2 = int(input('숫자2를 입력하세요 >> '))
    print(input1/input2)
# except ZeroDivisionError:
#     print('0으로 나눌수 없습니다.')
# except ValueError:
#     print('숫자가 아닙니다')
except Exception as e:
    print('에러의 이유는 : ', e)


print('프로그램 종료')