
# isdigit() , isalpha(), isalnum(), islower(), isupper(), isspace()

aa = '1234'

# 숫자 확인
if aa.isdigit():
    print('숫자입니다')
else:
    print('숫자가 아닙니다')

# 문자 
bb = 'abc1'
if bb.isalpha():
    print('문자입니다')
else:
    print('문자가 아닙니다')
    
# 문자 또는 숫자인지 (특수문자가 있는지 없는지)
cc ='a1b2c3'
if cc.isalnum():
    print('문자 또는 숫자입니다')
else:
    print('문자 또는 숫자가 아닙니다')

# 대문자인지 소문자인지    (영문에 대한 대소문자, 이외의것은 상관없다.)
dd = 'a1aaabbb'
if dd.islower():
    print('소문자입니다')
else:
    print('소문자가 아닙니다')

ee = 'AAB!C'
if ee.isupper():
    print('대문자입니다')
else:
    print('대문자가 아닙니다')
    

