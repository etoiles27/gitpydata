from stumanage.student import Student
# import stumanage.student as st

# 첫 화면에 보여지는 함수. 사용자가 선택한 번호로 리턴해준다. 
def screenPrint():
    print()
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력')
    print('2. 학생성적출력') 
    print('3. 학생검색출력')  
    print('4. 학생성적수정')  
    print('5. 학생성적삭제')  
    print('6. 학생등수처리')       
    print('0. 프로그램종료')     
    print('-'*25)
    choice = int(input('원하는 번호를 입력하세요.>> '))
    return choice

# 학생정보 입력하는 함수 
def stuInput(stuSave):
    while True:
        print('[ 학생성적프로그램 ]')
        stuname = input('학생이름을 입력하세요 (0. 종료)>> ')
        if stuname == '0': # 0을 입력하면 상위메뉴로 이동
            break
        kor = int(input("국어 성적을 입력하세요 >> "))
        eng = int(input("영어 성적을 입력하세요 >> "))
        stu = Student(stuname,kor,eng) # 학생 클래스를 생성해서 입력받은 값을 저장해준다. 
        print(stu.stuname) # 클래스의 __str__ 함수를 불러 정보를 출력한다.
        stuSave.append(stu) # stuSave리스트에 학생함수를 저장해준다. 
        print('{}.{} 학생이 저장되었습니다. '.format(stu.stuno,stu.stuname))
        print()
 
# 전체 학생 정보를 출력하는 함수        
def stuOutput(stuSave):
    print()
    print('[학생 성적 전체 출력]')
    print()
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
    print('-'*60)
    for stu in stuSave:
        print(stu) # 클래스의 __str__ 함수를 불러 정보를 출력한다.
        
# 학생을 검색하는 함수 
def stuSearch(stuSave):
    print()
    se_name=input('검색하고싶은 학생의 이름을 입력하세요 >> ')
    s1=Student(se_name,0,0)
    tmp = 0  # 학생이 존재하면 1, 존재하지 않으면 0
    for stu in stuSave:
        if s1 == stu: # 클래스 안에 만들어놓은 __eq__함수를 부른다. 같으면 True. 
            print()
            print('[{}학생 성적 출력]'.format(se_name))
            print()
            print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
            print('-'*60)
            print(stu) # 클래스의 __str__ 함수를 불러 정보를 출력한다. 
            tmp = 1
            break
    if tmp == 0:
        print('{}학생이 존재하지 않습니다. '.format(se_name))

# 검색된 학생의 성적을 수정하는 함수         
def stuModify(stuSave):
    print()
    modiName = input('수정을 원하는 학생의 이름을 입력하세요 >> ')
    s1=Student(modiName,0,0)
    scnt = 0 # 학생이 존재하면 1, 존재하지 않으면 0
    for stu in stuSave:
        if s1 == stu: # 학생이 존재하면, 
            scnt = 1  # 학생이 존재하기 때문에 scnt를 1로 바꿔준다 
            print('{}학생이 검색되었습니다.'.format(modiName))
            print('[ 점수 수정 ]')
            print('1.국어점수 수정')
            print('2.영어점수 수정')
            print('0.상위메뉴 이동')
            modiNum = int(input('원하는 메뉴를 선택하세요 >>'))
            if modiNum == 1: # 국어성적 수정
                print('국어성적 수정을 선택하셨습니다. ')
                # 현재 국어성적 출력
                print('현재 {}의 국어점수는 {}점 입니다.'.format(stu.stuname,stu.kor))
                modiScore = int(input("수정할 점수를 입력해주세요 >> "))
                stu.setKor(modiScore)
                #Student.setKor(stu,modiScore) # 클래스 내 setKor 함수를 호출해서 국어점수를 수정
            elif modiNum == 2: # 영어성적 수정
                print('영어성적 수정을 선택하셨습니다. ')
                # 현재 영어성적 출력
                print('현재 {}의 영어점수는 {}점 입니다.'.format(stu.stuname,stu.eng))
                modiScore = int(input("수정할 점수를 입력해주세요 >> "))
                Student.setEng(stu,modiScore) # 클래스 내 setEng 함수를 호출해서 국어점수를 수정
            elif modiNum == 0: # 상위메뉴로 이동
                break
   
            break
    if scnt == 0:
        print('{}학생이 존재하지 않습니다. '.format(modiName))

# 검색된 학생을 삭제하는 함수. 
def stuDel(stuSave):
    print()
    delName = input('삭제를 원하는 학생의 이름을 입력하세요 >> ')
    dcnt = 0  # 학생이 존재하면 1, 존재하지 않으면 0
    # stuSave리스트 안에 클래스 하나하나를 for문을 통해 본다.
    for i in range(len(stuSave)):
        # 만약에 stuSave[i]번째 클래스의 .stuname이 입력갑과 같을 경우
        if delName in stuSave[i].stuname:
            dcnt = 1 # 학생이 존재
            del(stuSave[i]) # 학생클래스를 리스트로부터 삭제한다. 
            print('{} 학생 정보가 삭제되었습니다.'.format(delName))
            break
    if dcnt == 0: # 학생이 존재하지 않으면
         print('{}학생이 존재하지 않습니다. '.format(delName))
         
# 등수처리 함수 
def stuRank(stuSave):
    for stu1 in stuSave:
        rcount = 1 # 등수를 카운트
        for stu2 in stuSave:
            # 학생 클래스에서 총점을 가져오는 함수를 사용해서 각각 비교 
            if stu1.getTotal() < stu2.getTotal():  
                rcount += 1 
        # 등수카운트가 끝나면 학생 클래스 내 setRank 함수를 통해서 rank값을 저장         
        stu1.setRank(rcount)
        # Student.setRank(stu1, rcount)
    print('등수처리를 완료했습니다. ')
             
