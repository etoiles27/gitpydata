
import stuclass as st

#stuSave=[]

# 학생성적 입력 실행시 보여지는 첫번째 페이지. 
# 사용자가 원하는 메뉴를 선택할 수 있다. 
def mainpage(choice):
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력')
    print('2. 학생성적수정') 
    print('5. 학생검색출력')     
    print('0. 프로그램종료')     
    print('-'*25)
    choice = input('원하는 번호를 입력하세요.>>')
    if not choice.isdigit():
        print(' 잘못 입력하셨습니다. 다시 입력해주세요. ')
        choice = 9
    else:
        choice = int(choice)
    
    return choice

# 학생 정보 입력 함수
def stu_input(stuSave):
    sCount = st.Student.getStuNo() # 몇번째 학생인지 보여지는 함수 출력
    print('-- {}번째 학생등록 -- '.format(sCount+1))
    sName = input('학생이름을 입력하세요.>>')
    kor = int(input('국어 점수를 입력하세요.>>'))
    eng = int(input('영어 점수를 입력하세요.>>')) 
    s1 = st.Student(sName,kor,eng) # 학생클래스에 입력된 정보를 저장 
    stuSave.append(s1) # 저장된 클래스를 리스트에 저장 
    
# 학생 정보 출력 함수     
def stu_all(stuSave):
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
    print('-'*60)
    for i in range(len(stuSave)):
        print(stuSave[i].stuNo,stuSave[i].stuName,stuSave[i].stuKor,stuSave[i].stuEng,stuSave[i].stuTotal,stuSave[i].stuAvg,stuSave[i].stuRank,sep='\t')

# 학생 성적 수정 함수 
def stu_modify(stuSave):
    modiName = input('수정을 원하는 학생의 이름을 입력하세요 >> ')
    scnt = 0
    for i in range(len(stuSave)):
        if modiName == stuSave[i].stuName:
            scnt = 1
            print('{}학생이 검색되었습니다.'.format(modiName))
            print('[ 점수 수정 ]')
            print('1.국어점수 수정')
            print('2.영어점수 수정')
            print('0.상위메뉴 이동')
            modiNum = int(input('원하는 메뉴를 선택하세요 >>'))
            if modiNum == 1:
                print('국어성적 수정을 선택하셨습니다. ')
                print('현재 {}의 국어점수는 {}점 입니다.'.format(stuSave[i].stuName,stuSave[i].stuKor))
                modiScore = int(input("수정할 점수를 입력해주세요 >> "))
                st.Student.modifyKor(stuSave[i],modiScore)
                #print(' 수정이 완료되었습니다. ')
            elif modiNum == 2:
                print('영어성적 수정을 선택하셨습니다. ')
                print('현재 {}의 국어점수는 {}점 입니다.'.format(stuSave[i].stuName,stuSave[i].stuEng))
                modiScore = int(input("수정할 점수를 입력해주세요 >> "))
                st.Student.modifyEng(stuSave[i],modiScore)
                #print(' 수정이 완료되었습니다. ')
            elif modiNum == 0:
                break
            
            
            break
    if scnt == 0:
        print('{}학생이 존재하지 않습니다. '.format(modiName))
            