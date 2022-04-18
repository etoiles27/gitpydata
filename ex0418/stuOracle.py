import cx_Oracle


#db 연결 함수
def myConn():
    #db 연결
    conn =cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
    return conn


def stuInsert():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    
    # 성적 입력받기 
    print('[학생성적입력]') # 완료
    stuname = input('학생이름을 입력하세요.>>')
    kor = int(input('국어 점수를 입력하세요.>>'))
    eng = int(input('영어 점수를 입력하세요.>>')) 
    math = int(input('수학 점수를 입력하세요.>>')) 
    
    #sql구문 실행 insert
    sql="insert into studata values(stu_seq.nextval,:1,:2,:3,:4,:5,:6,1)"
    rows=cs.execute(sql,(stuname,kor,eng,math,(kor+eng+math),(kor+eng+math)/3))
    print("insert: ",cs.rowcount)
    # sql닫기
    cs.close()
    conn.commit()
    conn.close()
    


def stuSelectAll():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    #sql구문 실행 SELECT
    sql = "select * from studata"
    rows=cs.execute(sql)
    print('-'*60)
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')  
  
    cs.close()
    conn.close()

def stuSelectByName():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    #sql구문 실행 SELECT
    stuname = input('학생이름을 입력하세요.>>')
    #sql =  "select * from studata where lower(stuname)='" +stuname.lower() +"'"
    sql =  "select * from studata where lower(stuname) like '%" +stuname.lower() +"%'"
    #sql =  "select * from studata where stuname like '%" +stuname +"%'"
    rows=cs.execute(sql)
    print('-'*60)
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)
    
    
    
    count = 0
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')  
        count = 1
                
    if count==0:
        print("학생이 존재하지 않습니다. ")
    cs.close()
    conn.close()    
        


def stuModify():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    #sql구문 실행 SELECT
    
    print('[ 학생성적 수정페이지 ]')
    print('-'*50)
    stuname = input('학생이름을 입력하세요.>>')
    sql =  "select * from studata where lower(stuname)='" +stuname.lower() +"'"
    rows=cs.execute(sql)
    print('-'*60)
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)
    count = 0
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')  
        count = 1
        
        
    if count==0:
        print("학생이 존재하지 않습니다. ")
        
    cur_kor=row[2]
    cur_eng=row[3]
    cur_math=row[4]
    
    print('[ 점수 수정 ]')
    print('1.국어점수 수정')
    print('2.영어점수 수정')
    print('3.수학점수 수정')
    print('0.상위메뉴 이동')
    searchNo = int(input('수정할 과목 번호를 입력하세요.>>'))
    if searchNo==1:
        print('현재 국어점수 :' , row[2])
        up_kor = int(input('변경할 국어점수 입력>>'))
        sql1="update studata set kor=:1,total=:2, avg=:3 where stuname=:4"
        rows1=cs.execute(sql1,(up_kor,(up_kor+cur_eng+cur_math),(up_kor+cur_eng+cur_math)/3,stuname))
        print("국어점수가 수정되었습니다. : ",cs.rowcount)
        
    elif searchNo==2:
        print('현재 영어점수 :' , row[3])
        up_eng = int(input('변경할 영어점수 입력>>'))
        sql1="update studata set eng=:1,total=:2, avg=:3 where stuname=:4"
        rows1=cs.execute(sql1,(up_eng,(cur_kor+up_eng+cur_math),(cur_kor+up_eng+cur_math)/3,stuname))
        print("국어점수가 수정되었습니다. : ",cs.rowcount)
    elif searchNo==3:
        print('현재 수학점수 :' , row[4])
        up_math = int(input('변경할 수학점수 입력>>'))
        sql1="update studata set math=:1,total=:2, avg=:3 where stuname=:4"
        rows1=cs.execute(sql1,(up_math,(cur_kor+cur_eng+up_math),(cur_kor+cur_eng+up_math)/3,stuname))
        print("국어점수가 수정되었습니다. : ",cs.rowcount)
    elif searchNo==0:
        print('상위메뉴로 이동합니다.')
        
    cs.close()
    conn.commit()
    conn.close()
      
    
    
def stuDel():
    
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    print('[학생성적삭제]') # 완료    
    stuname = input('학생이름을 입력하세요.>>')
    sql =  "select * from studata where lower(stuname)='" +stuname.lower() +"'"
    rows=cs.execute(sql)
    cnt = 0
    print('-'*60)
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)
    for row in rows:
        cnt+=1
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t') 
        
    if cnt>1:
        print("같은 이름의 학생이 여러명 입니다. 원하는 학생의 번호를 입력해주세요") 
        stunum = input(">>")
        
        flag = input("정말 삭제하시겠습니까? (삭제를 원하시면 y입력해주세요)")
        if flag == 'Y' or flag =='y':
            sql="delete from studata where stuno='"+stunum+"'"
            rows=cs.execute(sql)
            print("삭제되었습니다. ")
        else:
            print('삭제가 취소되었습니다.')

        # sql닫기
        cs.close()
        conn.commit()
        conn.close()
    
    
    
    
    
    
def stuRank():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    stuname = input('학생이름을 입력하세요.>>')
    #sql =  "select * from studata where lower(stuname)='" +stuname.lower() +"'"
    sql =  "select * from studata "
    #sql =  "select * from studata where stuname like '%" +stuname +"%'"
    rows=cs.execute(sql)
    print('-'*60)
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)
       
    
    count = 0
    for row in rows:
        if row[1].find(stuname) != -1:
            print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')  
            count = 1
        
        
    

def screenPrint():
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력') # 완료
    print('2. 학생성적수정') # 완료
    print('3. 학생성적삭제') # 완료
    print('4. 학생성적전체출력') # 완료
    print('5. 학생검색출력')     # 완료
    print('6. 등수처리')         
    print('0. 프로그램종료')     # 완료
    print('-'*25)
    # 숫자만 받는데, 문자를 입력하면 에러
    # 숫자만 받도록 변경
    choice = input('원하는 번호를 입력하세요.>>')
    # isdigit() 숫자인지아닌지 확인함수
    if not choice.isdigit():  # 숫자
        print('숫자만 입력가능합니다.!!')
    return int(choice)
