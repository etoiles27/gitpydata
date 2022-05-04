# 문자열 
# 문자열은 list 처럼 사용할 수 있다. -> 인덱싱, 슬라이싱이 가능하다. 
# 문자열 길이에 len함수를 쓸 수 있다. 

# a ='안녕하세요'
# alist=[1,2,3,4,5]
# print(alist[0])
# print(a[0])

# b = "나비와 구름"
# print(b[3])

# print(len(a)) # 문자로 len을 사용 할 수 있다 
# print(len(b)) # 빈 공간도 포함이다. 

# str1 = '안녕하세요. 파이썬입니다. '
# print(str1[7:])


alist =[123,46,3456,483,1,50,111,33333,9,1000000]
numlist=['짝수','홀수']
# # 123: 홀수 .. 출력
# for i in range(len(alist)):
#     if alist[i]%2==0:
#         print('{:7d} : {}'.format(alist[i], '짝수'))
#     else:
#         print('{:7d} : {}'.format(alist[i], '홀수'))

# for i in alist:
#     if i%2 == 0:
#         print('{}[{}]:{}'.format(i,len(str(i)),'짝수'))
#     else:
#         print('{}[{}]:{}'.format(i,len(str(i)),'홀수'))

# for i in alist:
#     print('{}[{}자리]:{}'.format(i,len(str(i)),numlist[i%2]))
    

# 주민번호 뒷자리를 입력받아 남자,여자출력하세요
# 7자리가 아니면 다시 입력받음
# 990101-1105555
list1=['여자','남자']

while True:
    ssn = input('주민번호 뒷자리(7숫자)를 입력하세요 >>  ')
    if ssn.isdigit():
        if len(ssn)==7:
            ssn_int=int(ssn[0])
            #print(list1[ssn_int%2])
            
            if ssn_int==2 or ssn_int==4:
                print('여자')
            elif ssn_int==1 or ssn_int==3:
                print('남자')
            else:
                print('잘못입력하셨습니다. 다시 입력하세요')
        else:
            print("7 자리가 아닙니다. 다시 입력하세요")
            
    else:
        print("숫자가 아닙니다. 다시 입력하세요")
        