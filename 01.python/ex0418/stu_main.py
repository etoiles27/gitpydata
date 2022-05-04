#1,2,4,5

from stuOracle import *

while True:
    # 화면 출력
    choice = screenPrint()
    if choice == 1 : # 1. 학생성적입력
        stuInsert()
    elif choice == 2 : # 2. 학생성적수정
        stuModify()    
    elif choice == 3 : # 3. 학생검색삭제
        stuDel()  
    elif choice == 4 : # 4. 학생성적전체출력
        stuSelectAll()
    elif choice == 5 : # 5. 학생성적검색출력
        stuSelectByName()
    elif choice == 6 : # 6. 학생등수처리
        stuRank()
    elif choice == 0 : #0. 프로그램종료
        print('프로그램을 종료합니다. ')
        break
    else:
        pass


