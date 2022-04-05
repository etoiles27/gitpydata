# 화면 출력 구성 
# 1. 입력, 2.수정, 3. 삭제..
# 프로그램을 무한반복 
# 성적 입력부분 구성 

# 학생 성적 입력프로그램
# 학생정보 : 
# 번호, 이름, 국어, 영어, 합계, 평균, 등수 

stSave = [] #[[0]*7 for _ in range(0,10)]

print(stSave)
st_cnt = 0
while True:
    chice = 0 
    print('-'*35)
    print('[\t학생성적입력 프로그램\t]')
    print('-'*35)
    print(' 1. 학생성적 입력')
    print(' 2. 학생성적 수정')
    print(' 3. 학생성적 삭제')
    print(' 4. 학생전체 출력')
    print(' 5. 학생검색 출력')
    print(' 6. 등수처리')
    print(' 0. 프로그램 종료 ')
    print('-'*35)
    choice = input(' 원하는 번호를 입력하세요 >> ')
    if not choice.isdigit():
        print('숫자만 입력이 가능합니다')
        continue
    choice = int(choice)
    print('*'*35)
    print('-'*35)
    if choice == 1:
        print('{}번째 학생 입력'.format(st_cnt+1))
        
        sName = input('학생의 이름을 입력해주세요 >> ')
        sKor = int(input('학생의 국어점수를 입력해주세요 >> '))
        sEng = int(input('학생의 영어점수를 입력해주세요 >> '))
        
        temp = [st_cnt+1,sName,sKor,sEng,sKor+sEng,(sKor+sEng)/2,0  ]
        stSave.append(temp)
       
        st_cnt += 1 
        
    
        
    elif choice == 2:
        print(' 2. 학생성적 수정')
    elif choice == 3:
        print(' 3. 학생성적 삭제')
        # delno = int(input("삭제를 원하는 학생 번호를 입력하세요 >> "))
        # print(' 삭제를 원하시는 학생 정보 입니다. {}'.format(stSave[delno-1]))
        # del(stSave[delno-1])
        del_name = input('삭제하고자 하는 학생의 이름을 입력해주세요 >> ')
        ans = 0
        for idx, stu in enumerate(stSave):
            if del_name in stu:
                print('삭제하고자 하는 학생 정보입니다. {}'.format(stSave[idx]))
                ans = int(input('삭제를 원하시면 1을 눌러주세요 >> '))
                if ans == 1:
                    del(stSave[idx])
        
    elif choice == 4:
        print(' 입력된 학생 정보 입니다 >> ')
        print('-'*60)
        # for i in range(len(stSave)):
        #     print("{}번 \t이름: {} \t국어: {} \t영어: {} \t합계: {} \t평균 : {} \t등수 : {}".format(stSave[i][0],stSave[i][1],stSave[i][2],stSave[i][3],stSave[i][4],stSave[i][5],stSave[i][6] ))
        print("번호 \t이름 \t국어 \t영어 \t합계 \t평균 \t등수")
        print('-'*60)
        for stu in stSave:
            for i in stu:
                print(i, end = '\t')
            print()
            print()
        print('-'*60)
                  

        
    elif choice == 0:
        print("프로그램을 종료합니다")
        break
        
        
    