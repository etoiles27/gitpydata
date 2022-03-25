

# 학생 성적 프로그램. (무한 루프)

stu_data = []
u_choice = 0 
stu_count = 0
while True:

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
    u_choice = int(input('원하는 번호를 입력하세요 >>  '))
    print("*"*35)
    
    if u_choice == 1: # 학생 성적 입력 
        print('{}번 학생 등록 >> '.format(stu_count+1))
        stu_name = input('학생 이름을 입력해주세요 >> ')
        stu_kor = int(input('학생의 국어점수를 입력해주세요 >> '))
        stu_eng = int(input('학생의 영어점수를 입력해주세요 >> '))
        stu_total = stu_kor+stu_eng
        stu_avg = stu_total/2
        stu_rank = 0
        tmp = {'stu_no':stu_count+1, 'stu_name':stu_name, 'stu_kor':stu_kor,'stu_eng':stu_eng,'stu_total':stu_total,'stu_avg':stu_avg,'stu_rank':stu_rank}
        stu_data.append(tmp)
        print('학생 성적이 저장되었습니다. ')
        print("*"*35)        
        stu_count += 1 # 학생 번호 증가 
        
    elif u_choice == 2: # 학생성적수정
        search_name = input('수정을 원하는 학생 이름을 입력해 주세요 >> ')
        count = 0 # 학생 정보에 학생이 존재하는지 카운트
        for i, stu in enumerate(stu_data):
            if search_name in stu.values():
                count += 1
                print('-'*35)
                print('[ 학생 성적 수정 ] ')
                print('1. 국어점수 수정 ')
                print('2. 영어점수 수정 ')
                print('0. 상위 메뉴로 이동 ')
                print('-'*35)
                input_kor=stu['stu_kor']
                input_eng=stu['stu_eng']
                u_ch = 0
                u_ch = int(input('원하는 번호를 선택해주세요 '))
                if u_ch == 1:
                    print('{} 학생의 국어점수는 {} 점입니다.'.format(stu['stu_name'],stu['stu_kor']))
                    input_kor = int(input('수정할 점수를 입력해 주세요 >> ')) 
                    stu['stu_kor'] = input_kor 
                elif u_ch == 2:
                    print('{} 학생의 영어점수는 {} 점입니다.'.format(stu['stu_name'],stu['stu_eng']))
                    input_eng = int(input('수정할 점수를 입력해 주세요 >> ')) 
                    stu['stu_eng'] = input_eng
                elif u_ch == 0:
                    break
                stu['stu_total'] = input_kor+input_eng
                stu['stu_avg']=(input_kor+input_eng)/2
                print('{} 학생 정보가 수정되었습니다.'.format(search_name))
                
                
        if count ==0:
            print('{} 학생 정보가 존재하지 않습니다.'.format(search_name))
            break
                
        
    elif u_choice == 3: # 학생성적삭제
        input_name = input('삭제를 원하는 학생 이름을 입력해 주세요 >> ')
        count = 0 # 학생이 리스트에 존재하는지 카운트
        for i, stu in enumerate(stu_data):
            if input_name in stu.values():
                del(stu_data[i])
                print('{} 학생 정보가 삭제되었습니다.'.format(input_name))
                count += 1
        if count == 0:
            print('{} 학생 정보가 존재하지 않습니다.'.format(input_name))
            break      
    elif u_choice == 4: # 학생성적출력
        print('-'*50)
        print('\t[ 전체 학생 성적 정보]')
        print('-'*50)
        print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
        for stu in stu_data:
            for k, v in stu.items():
                print('{}\t'.format(v),end='')
            print()
        print()
    elif u_choice == 5:   # 특정학생정보 검색 
        ser_name = input('검색을 원하는 학생 이름을 입력해 주세요 >> ')  
        count = 0 # 학생이 리스트에 존재하는지 카운트
        for i, stu in enumerate(stu_data):
            if ser_name in stu.values():
                print('-'*50)
                print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
                print('-'*50)
                print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu['stu_no'],stu['stu_name'],stu['stu_kor'],stu['stu_eng'],stu['stu_total'],stu['stu_avg'],stu['stu_rank']))
                count += 1
        if count == 0:
            print('{} 학생 정보가 존재하지 않습니다.'.format(ser_name))
            break
    elif u_choice==6: #등수처리
        score_list =[]
        ranked_score=[]
        ranklist=[]
        for stu in stu_data:
            score_list.append(stu['stu_avg'])
            ranked_score.append(stu['stu_avg'])
        
        ranked_score.sort(reverse=True)
        
        for i in score_list:
            cnt = 1
            sameScore = False
            for j in range(len(ranked_score)):
                if i != ranked_score[j]:
                    cnt += 1
                else:
                    if sameScore == False:
                        ranklist.append(cnt)
                        sameScore = True
        
        
        for i, stu in enumerate(stu_data):
            stu['stu_rank'] = ranklist[i]
            
            
        print('등수가 반영되었습니다. !! ')


    
        
    elif u_choice == 0: # 프로그램 종료    
        print('프로그램을 종료합니다')
        print("*"*35)
        break
    