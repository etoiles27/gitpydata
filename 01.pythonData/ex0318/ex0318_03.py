
# str1 = '서울인재개발원 파이썬수업'
# for i in range(len(str1)):
#     if i == len(str1)-1: # 마지막 쉼표는 빼주세요 
#         print(str1[i],end='')
#     else:
#         print(str1[i]+',',end='')



# instr,outstr='',''
# count, i = 0, 0

# instr=input("원하는 글자를 입력하세요 >> ")
# count = len(instr)

# # 거꾸로입력. (문자열은 더하기를사용해도된다 (리스트의경우에는 append사용함))
# for i in range(count):
#     outstr += instr[(count-1)-i]

# print(outstr)


# list1=[10,4,3,9,20,21]
# list2 = [21, 20, 9, 3, 4, 10] # 역순출력
# list3 = [3, 4, 9, 10, 20, 21] # 순차정렬
# list4 = [21, 20, 10, 9, 4, 3] # 역순정렬 

# print(list1)
# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)


str1 = 'Python iS Easy'
# print(str1.upper()) # 대문자 출력
# print(str1.lower()) # 소문자 출력
# print(str1.swapcase()) # 대->소, 소->대 변경 출력
# print(str1.title()) # 단어 첫글자를 대문자로
# print(str1.isupper()) # 첫글자가 대문자인지
# print(str1[8].isupper()) # n번째 글자가 대문자인지
# print(str1.find('b')) # n번방에 't'가 있음을 알려준다 (잇을때 인덱스번호를 , 없으면 -1 출력)
# print(str1.index('t')) # n번방에 't'가 있음을 알려준다(잇을때 인덱스번호를 , 없으면 error -> 자동종료)
# print(str1.count('s')) # 글자의 개수를 세준다 (대소문자 구분한다)
# print(str1.startswith('P')) # 첫글자가 뭐로 시작하는지 알 수 있다. 
# print(str1.endswith('f')) #끝 글자가 뭐로 끝나는지 알 수 있다 .


# # 대소문자 구분없는 단어를 검색하는 방법 
# str2 = str1.lower()
# print(str2.count('s'))

# in_str = input('문자를 입력하세요')
# if in_str.lower() in str1.lower():
#     print('{}는 {}개 존재합니다'.format(in_str,str1.lower().count(in_str)))
# else:
#     print('{}라는 글자는 존재하지 않습니다.'.format(in_str))

