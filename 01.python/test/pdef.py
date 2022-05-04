

import os
import json

stuSave=[] # 입력된 학생을 저장하는 list로 딕셔너리로 이루어짐 [{학생1정보},{학생2정보}]
global stuCount # 입력된 학생 수를 저장하는 변수 
StuCount = 0
jsonfilename = 's.json'
# json save
def jsonSave():
    json.dump(stuSave,open(jsonfilename,'w'))
# json read
def jsonRead():
    if not jsonfilename in os.listdir():
        json.dump(stuSave,open(jsonfilename,'w'))
    else:
        json.load(open(jsonfilename))
        

# 학생카운트
def StuCount():
    pass

# 화면 출력 함수 호출
def screen_print():
    jsonRead()
    #cnt = stuCount()
    u_choice = 0
    print("*"*35)
    print('[ 학생성적프로그램 ]')
    print("*"*35)
    print('1. 학생성적 입력')
    print('2. 학생성적 수정')
    print('3. 학생성적 삭제')
    print('4. 학생성적 출력')
    print('5. 학생 검색')
    print('6. 등수 처리')
    print('0. 프로그램종료')
    print("*"*35)
    u_choice = input('원하는 번호를 입력하세요 >>  ')
    print("*"*35)
    if not u_choice.isdigit():
        print('숫자를 입력하세요')
        u_choice = 9
    else:
        u_choice=int(u_choice)
    return u_choice

 # 학생 성적 입력 
def stu_input():
    pass

 # 학생성적수정
def stu_modify(): 
    pass
# 학생성적삭제
def stu_delete():
    pass
# 학생성적출력
def stu_print():
    pass
# 특정학생정보 검색 
def stu_search():
    pass
#등수처리    
def stu_rank():
    pass