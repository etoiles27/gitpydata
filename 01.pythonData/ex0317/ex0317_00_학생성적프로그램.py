
# 학생 성적 입력프로그램
# 학생정보 : 
# 번호, 이름, 국어, 영어, 합계, 평균, 등수 

# 학생정보를 딕셔너리로 저장
stuSave = [] #
stu_cnt = 0 # 학생가입인원 확인 카운트
while True:
    print("*"*35)
    print('[ 학생성적프로그램 ]')
    print("*"*35)
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생성적출력')
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
        temp = {'stuno': stu_cnt+1 ,'stuname':sName,'kor':sKor,'eng':sEng,'total':(sKor +sEng),'avg':(sKor +sEng)/2,'rank':0}
        stuSave.append(temp)
        print('학생성적이 저장되었습니다. >>')
        #print(stuSave)
        stu_cnt += 1 # 학생번호 1 증가       
    elif choice == 2:
        print('학생성적수정을 선택하셨습니다. >>')
        search_name = input('수정할 이름을 입력하세요 (상위메뉴 이동: 0)>> ')
        count = 0
        for i, stu in enumerate(stuSave):
            if search_name in stu.values(): 
                # 국어점수 수정, 영어점수 수정  (여기에선 이름이 primary key 로 수정불가하다는 가정)
                print('{} 학생이 검색되었습니다.'.format(search_name))
                print('[ 점수 수정 ] ')
                print('1. 국어점수 수정')
                print('2. 영어점수 수정')
                print('0. 상위메뉴 이동')
                search_no=int(input('원하는 번호를 선택하세요. >> '))
                if search_no ==1:
                    print('현재 국어 점수는 {} 점 입니다. '.format(stu['kor']))
                    kor_score = int(input('국어점수를 몇점으로 수정하시겠습니까? >> '))
                    stu['kor'] = kor_score
                    stu['total'] =  stu['kor']+stu['eng']
                    stu['avg'] =  (stu['kor']+stu['eng'])/2
                elif search_no ==2:
                    print('현재 영어 점수는 {} 점 입니다. '.format(stu['eng']))
                    eng_score = int(input('영어점수를 몇점으로 수정하시겠습니까? >> '))
                    stu['eng'] = eng_score
                    stu['total'] =  stu['kor']+stu['eng']
                    stu['avg'] =  (stu['kor']+stu['eng'])/2
                elif search_no == 0:
                    print('상위메뉴로 이동합니다. ')
                    break    
                print('{} 학생 정보가 수정되었습니다.'.format(search_name))
                count += 1
                break
            if count == 0:
                print('{} 학생이 없습니다.'.format(search_name))
        if search_name == 0:
            break
    elif choice == 3:
        print('학생성적삭제를 선택하셨습니다. >>')
        search_name = input('삭제할 이름을 입력하세요 >> ')
        count = 0
        for i, stu in enumerate(stuSave):
            if search_name in stu.values(): 
                del(stuSave[i])
                print('{} 학생 정보가 삭제되었습니다.'.format(search_name))
                count += 1
                break
            if count == 0:
                print('{} 학생이 없습니다.'.format(search_name))
    elif choice == 4:
        print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
        print('-'*50)
        for stu in stuSave:
            for k, v in stu.items():
                print('{}\t'.format(v),end=' ')
            print()
        print()
    elif choice == 0:
        print("프로그램을 종료합니다")
        break


