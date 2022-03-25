id = 'aaa'
pwd = '1111'

user_id = input('아이디를 입력하세요 : ')
user_pwd = input('패스워드를 입력하세요 : ')

# if id == user_id:
#     print('아이다가 같습니다')
#     if pwd == user_pwd:
#         print('패스워드가 같습니다')
#         print('로그인 되었습니다!')
#     else:
#         print('비밀번호가 불일치합니다 \n다시 입력하세요')
# else:
#     print('아이디가 일차하지 않습니다. \n다시 입력하세요')

# if id == user_id and pwd == user_pwd:
#     print('아이디, 패스워드가 일치합니다')
# else:
#     print('아이디 또는 패스워드가 일치하지 않습니다 \n다시입력하세요')
    
# if id != user_id and pwd != user_pwd:
#     print('아이디 또는 패스워드가 일치하지 않습니다 \n다시입력하세요')
# else:
#     print('아이디, 패스워드가 일치합니다')
    
if not(id == user_id and pwd == user_pwd):
    print('아이디 또는 패스워드가 일치하지 않습니다 \n다시입력하세요')
else:
    print('아이디, 패스워드가 일치합니다')
    

# != 는 같지 않음을 의미한다 
# 논리연산자는 and or not 이 있다. 
# and는 둘다 같을경우만 참이다. or는 둘중에 한개만 참일 경우에도 참이다. 