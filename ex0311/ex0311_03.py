# 전역변수와 지역변수 

score = int(input('점수를 입력하세요 : '))
msg =''
# if score>=60:
#     msg = '합격'
# else:
#     msg = '불합격'

# 한줄 if문
msg='합격' if score>=60 else '불합격'

print(msg)