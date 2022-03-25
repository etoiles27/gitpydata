
# a =int(input('정수를 입력하세요 >> '))
# print(a)

# try:
#     a =int(input('정수를 입력하세요 >> '))
#     print(a)
# except:
#     print('프린트 정상')

while True:
    try:
        a =int(input('정수를 입력하세요 >> '))
        if a == 0:
            break
        print(a)
    except Exception as err:
        print(err)