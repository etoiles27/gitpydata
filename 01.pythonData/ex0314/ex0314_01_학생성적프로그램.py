
# 학생 성적 입력프로그램
# 학생정보 : 
# 번호, 이름, 국어, 영어, 합계, 평균, 등수 

stuSave = [[0]*7 for _ in range(10)] # 10 명의 학생입력공간 생성 
print(stuSave)

stu_cnt = 0 # 학생가입인원 확인 카운트
while True:
    print("*"*35)
    print('[ 학생성적프로그램 ]')
    print("*"*35)
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('0. 프로그램종료')
    print("*"*35)
    choice = int(input('원하는 번호를 입력하세요 >>  '))
    print("*"*35)
    
 
    if choice == 1:
        # print('학생성적입력을 선택하셨습니다. >>')
        print('{} 번째 학생 등록 >>'.format(stu_cnt+1))
        
        sName = input("학생이름을 입력해주세요 >> ")
        sKor = int(input("학생의 국어 점수를 입력해주세요 >> "))
        sEng = int(input("학생의 영어 점수를 입력해주세요 >> "))
        stuSave[stu_cnt][0] = stu_cnt+1       
        stuSave[stu_cnt][1] = sName # 학생이름 입력
        stuSave[stu_cnt][2] = sKor
        stuSave[stu_cnt][3] = sEng
        stuSave[stu_cnt][4] = sKor +sEng
        stuSave[stu_cnt][5] = (sKor +sEng)/2 
        print('학생성적이 저장되었습니다. >>')
        print(stuSave)
        stu_cnt += 1 # 학생번호 1 증가 
        
        
        
        
    elif choice == 2:
        print('학생성적수정을 선택하셨습니다. >>')
    elif choice == 3:
        print('학생성적삭제를 선택하셨습니다. >>')
    elif choice == 0:
        print("프로그램을 종료합니다")
        break


