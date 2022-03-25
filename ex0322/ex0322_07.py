# 학생 성적 프로그램
# 3명의 학생의 성적을 입력받아
# 번호, 이름, 국어, 영어, 합계, 평균, 등수 

# [학생성적프로그램]
# 1. 학생성적 입력
# 2. 학생파일 저장
# 3. 학생파일 읽기
# 4. 학생성적모두출력
#-------------------
# 원하는 번호를 입력하세요 
# 3명 입력하고, 
# 학생성적 모두 출력
# 1명 더 입력
# 파일 저장
# 파일 읽기
# 출력
import json 


choice = 0 
Students=[]
scnt = 0
while True:
        
    print('[학생성적프로그램]')
    print('1. 학생성적 입력')
    print('2. 학생파일 저장')
    print('3. 학생파일 읽기')
    print('4. 학생성적 모두출력')
    print('0. 프로그램 종료')
    print('-'*50)
    choice = int(input("원하는 번호를 선택하세요 >> "))
    print('-'*50)
    
    # 1. 학생성적 입력
    if choice == 1:
        # 번호, 이름, 국어, 영어, 합계, 평균, 등수 
        student={}
        sName , sKor, sEng ,sTotal ,sAvg, sRank = 0,0,0,0,0,0
        sName = input('학생 이름을 입력하세요 >> ')
        sKor = int(input('학생 국어점수를 입력하세요 >> '))
        sEng = int(input('학생 영어점수를 입력하세요 >> '))
        student['number'] = scnt+1
        student['name'] = sName
        student['kor'] = sKor
        student['eng'] = sEng
        student['total'] = sKor+sEng
        student['avg'] = (sKor+sEng)/2
        student['rank'] = 0
        Students.append(student)
        scnt +=1
    
    #2. 학생파일 저장    
    elif choice ==2:
        json.dump(Students,open('studentInfo.json','w'))
        with open('student.txt','w',encoding='utf-8') as file:   
            # for stu in Students:
            #     cnt = 0
            #     for k in stu.keys():
            #         if cnt !=0 :
            #             file.write(',')
            #         file.write(k)
            #         cnt +=1
            #     break 
            file.write('번호,이름,국어,영어,합계,평균,등수')
            file.write('\n') 
            for stu in Students:
                cnt = 0
                for v in stu.values():
                    if cnt !=0 :
                        file.write(',')
                    file.write(str(v))
                    cnt+=1
                file.write('\n')
    
    # 3. 학생파일 읽기
    elif choice == 3:
        # txt version 
        with open('student.txt','r',encoding='utf-8') as file:
            lines=file.readlines()
            for line in lines:
                print(line,end='')
        # json ver 
        stu_data = json.load(open('studentInfo.json'))
        print(stu_data)
    # 4. 학생성적모두출력
    elif choice ==4:
        print('-'*50)
        print('[ 전체 학생 성적 ]')
        print('-'*50)
        print('번호\t이름\t국어\t영어\t합계\t평균\t등수')
        for stu in Students:
            for v in stu.values():
                print(v,end='\t')
            print()
            
    elif choice == 0 :
        print(Students)
        break
    
 
