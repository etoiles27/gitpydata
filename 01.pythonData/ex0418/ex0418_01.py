
import cx_Oracle


#db 연결 함수
def myConn():
    #db 연결
    conn =cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
    return conn


# select 함수 호출
def mySelect():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    #sql구문 실행 SELECT
    rows=cs.execute("select * from studata")
    print('-'*60)
    print('번호','이름','국어','영어','수학','합계','평균','등수',sep='\t')  
    print('-'*60)
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],sep='\t')  
  
    cs.close()
    conn.close()
    
# insert 함수 호출    
def myInsert():
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
    
# update 함수 호출
def myUpdate():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    print('[학생성적수정]') # 완료
    stuname = input('학생이름을 입력하세요.>>')
    kor = int(input('국어 점수를 입력하세요.>>'))
    eng = int(input('국어 점수를 입력하세요.>>'))
    math = int(input('국어 점수를 입력하세요.>>'))
    sql="update studata set kor=:1, eng=:2, math=:3, total=:4, avg=:5 where stuname=:6"
    rows=cs.execute(sql,(kor,eng,math,(kor+eng+math),(kor+eng+math)/3,stuname))
    print("update: ",cs.rowcount)
    # sql닫기
    cs.close()
    conn.commit()
    conn.close()
    
# delete 함수 호출
def myDelete():
    conn = myConn() #db연결 
    #실행선언
    cs=conn.cursor()
    print('[학생성적삭제]') # 완료    
    stuname = input('학생이름을 입력하세요.>>')
    sql="delete from studata where stuname='"+stuname+"'"
    #sql="delete studata where stuname=:1"
    rows=cs.execute(sql,stuname)
    print()
    # sql닫기
    cs.close()
    conn.commit()
    conn.close()
    
    
#mySelect()
#myInsert()
#myUpdate()
myDelete()