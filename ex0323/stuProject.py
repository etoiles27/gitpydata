
from stu_def import *
import json

# 학생 성적 프로그램. (무한 루프)

# stu_data = jsonRead() # 학생 데이터 저장리스트
# stu_count = stuCount() # 학생 수 카운트 
while True:
    u_choice = 0 #화면 출력에 대한 선택번호 변수 
    u_choice= screen_print() # 화면 출력 함수 호출
    if not u_choice.isdigit():
        print('숫자가 아닙니다. 다시 입력해주세요')
        continue
    u_choice = int(u_choice)
    if u_choice == 1: # 학생 성적 입력 
        stu_input()   
    elif u_choice == 2: # 학생성적수정
        stu_modify()                    
    elif u_choice == 3: # 학생성적삭제
        stu_delete()    
    elif u_choice == 4: # 학생성적출력
        stu_print()
    elif u_choice == 5: # 특정학생정보 검색 
        stu_search()
    elif u_choice==6: #등수처리    
        stu_rank()
    elif u_choice == 0: # 프로그램 종료    
        print('프로그램을 종료합니다')
        print("*"*35)
        break
    