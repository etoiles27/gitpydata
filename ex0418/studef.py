import cx_Oracle


#db 연결 함수
def myConn():
    #db 연결
    conn =cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
    return conn



stuSave=[]



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
    sql = "select * from studata where stuname='"+stuname+"'"
    rows=cs.execute(sql)
    print('-'*60)
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')  
        
        


def stuModify():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    #sql구문 실행 SELECT
    
    print('[ 학생성적 수정페이지 ]')
    print('-'*50)
    stuname = input('수정할 이름을 입력하세요.>>')
    sql = "select * from studata where stuname='"+stuname+"'"
    rows=cs.execute(sql)
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')  
        
        
    
    
def stuDel():
    return;
def stuRank():
    return;

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
