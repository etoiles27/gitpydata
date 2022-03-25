# 함수와 모듈

# def mul(n1,n2):
#     print(n1+n2)
#     print(n1-n2)
#     print(n1*n2)
#     print(n1/n2)

# for i in range(3):
    
#     num1 = int(input('숫자를 입력하세요 >> '))
#     num2 = int(input('숫자를 입력하세요 >> '))
#     mul(num1,num2)
#     print('-'*20)




# print(num1*1+num2)
# print(num1*1-num2)
# print(num1*1*num2)
# print(num1*1/num2)

# num3 = int(input('숫자를 입력하세요 >> '))
# num4 = int(input('숫자를 입력하세요 >> '))
# print(num3*2+num4)
# print(num3*2-num4)
# print(num3*2*num4)
# print(num3*2/num4)


def coffee_machine(choice):
    
    print("[ 커피주문 완료 ]")
    print("1. 종이컵 준비합니다.")
    print("2. 물을 보충합니다.")
    print("3. 커피를 내립니다.")

    if choice == 1:
        print('4. 커피를 컵에 추가합니다.')
        print('아메리카노 완성 !! ')
    elif choice ==2:
        print('4. 커피를 한번 더 내린 후 컵에 추가합니다.')
        print('아메리카노 2샷 완성 !! ')
    elif choice ==3:
        print('4. 커피를 컵에 추가고 얼음을 보충합니다.')
        print('아이스 아메리카노 완성 !!')

    print('5. 포장을 한 후 진동벨을 누릅니다.')



while True:

    choice = 0
    print("1. 아메리카노 \t2.아메리카노 2샷 \t3.아이스 아메리카노")
    choice = int(input("커피를 선택하세요 (0. 프로그램종료)>> "))
    if choice == 0:
        break
    coffee_machine(choice)
    

