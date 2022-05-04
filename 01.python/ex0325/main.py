#학생 관리 폴더 - 학번, 이름, 전화번호, 주소, 성별, 학년, 학과 .... 

#학생 성적 폴더 - 학번, 국어, 영어, 수학, 합계, 평균, 등수 .... 

from stumanage.student import Student 
from stumanage.studef import *
 
stuSave=[]
while True:
    # 화면 출력
    choice = screenPrint()
    if choice == 1 : # 1. 학생성적입력
        stuInput(stuSave)
    elif choice == 2 : # 2. 학생성적출력
        stuOutput(stuSave)
    elif choice == 3 : # 3. 학생검색출력
        stuSearch(stuSave)
    elif choice == 4 : # 4. 학생성적수정
        stuModify(stuSave)    
    elif choice == 5 : # 5. 학생성적삭제
        stuDel(stuSave)  
    elif choice == 6 : # 6. 학생등수처리
        stuRank(stuSave)
    elif choice == 0 : #0. 프로그램종료
        print('프로그램을 종료합니다. ')
        break
    else:
        pass




# s1 = Student(1,'홍길동',100,100)
# s2 = Student(2,'이순신',100,100)
# s3 = Student(3,'홍길동',10,90)
# print(s1.stuname)
# s1.setKor(200)
# print(s1.getKor())
# print(s1.kor)

# if s1==s3:
#     print('같다')
# else:
#     print('다르다')