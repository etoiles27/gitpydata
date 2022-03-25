import json
import os 


stu_data =[]
jasonname = 'stuData2.json'
global sCount 
def jsonRead():
    global stu_data
    stu_data = json.load(open(jasonname))
def jsonSave():
    json.dump(stu_data,open(jasonname,'w'))
#학생번호 증가함수
def stuCount():
    if not stu_data:
        return 0
    else:
        return stu_data[-1]['stu_no']

# 화면 출력 함수 
def screen_print():
    if not jasonname in os.listdir():
        jsonSave()
    jsonRead()
    #cnt = stuCount()
    u_choice = 0
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
    u_choice = input('원하는 번호를 입력하세요 >>  ')
    print("*"*35)
    return u_choice

# 성적 입력함수    
# json으로 리스트 이동없이 데이터 읽는 방법
def stu_input():
    # jsonRead()
    stu_count = 0
    stu_count = stuCount()
    
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
    jsonSave()
    
    


# 학생 성정 수정
def stu_modify():
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
            jsonSave()
            print('{} 학생 정보가 수정되었습니다.'.format(search_name))        
    if count ==0:
        print('{} 학생 정보가 존재하지 않습니다.'.format(search_name))
        
# 입력 학생 정보 삭제    
def stu_delete():
    jsonRead()
    input_name = input('삭제를 원하는 학생 이름을 입력해 주세요 >> ')
    count = 0 # 학생이 리스트에 존재하는지 카운트
    for i, stu in enumerate(stu_data):
        if input_name in stu.values():
            del(stu_data[i])
            jsonSave()
            print('{} 학생 정보가 삭제되었습니다.'.format(input_name))
            count += 1
    if count == 0:
        print('{} 학생 정보가 존재하지 않습니다.'.format(input_name))

# 학생 전체 성적정보 출력           
def stu_print():
    jsonRead()
    print()
    print('\t[ 전체 학생 성적 정보]')
    print('-'*55)
    print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
    print('-'*55)
    for stu in stu_data:
        for k, v in stu.items():
            print('{}\t'.format(v),end='')
        print()
    print()
    
# 특정학생정보 검색 
def stu_search():
    jsonRead()
    ser_name = input('검색을 원하는 학생 이름을 입력해 주세요 >> ')  
    count = 0 # 학생이 리스트에 존재하는지 카운트
    for i, stu in enumerate(stu_data):
        if ser_name in stu.values():
            print('-'*55)
            print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
            print('-'*55)
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu['stu_no'],stu['stu_name'],stu['stu_kor'],stu['stu_eng'],stu['stu_total'],stu['stu_avg'],stu['stu_rank']))
            count += 1
    if count == 0:
        print('{} 학생 정보가 존재하지 않습니다.'.format(ser_name))
# 등수처리
def stu_rank():
    jsonRead()
    for stu in stu_data:
        rcount = 1 #등수 
        for stu2 in stu_data:
            if stu['stu_total'] < stu2['stu_total']: # 점수비교
                rcount += 1 #stu2가 더 클경우 1 증가 
        stu['stu_rank'] = rcount # 등수입력
    jsonSave()
    print('등수처리가 완료되었습니다. !! ')