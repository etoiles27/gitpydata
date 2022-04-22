import cx_Oracle

def connectDB(): # db 연결함수
    conn =cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
    return conn

def closeDB(cs,conn): # db 저장하고 연결 끊기. 
    cs.close()
    conn.commit()
    conn.close()

def createTableDB(tbname): # 테이블 만들기 
    conn = connectDB() #db 연결함수 호출  
    cs=conn.cursor() # 실행선언
    sql = "create table "+tbname+"(sno number(4) primary key, sname varchar2(10) not null,sadd varchar2(100),sphone char(11),sbirth date,gender char(1) check(gender in('M','F')))"
    cs.execute(sql)
    closeDB(cs,conn)
    
def insertDB(tbname): # insert 하기 
    conn = connectDB() #db 연결함수 호출  
    cs=conn.cursor() # 실행선언
    # stumem -> sno, sname, sadd, sphone, sbirth, gender
    sql="insert into "+ tbname +" values(st_seq.nextval,:1,:2,:3,:4,:5)"
    cs.execute(sql, ('홍길순','서울시 구로구','01011111111','20000101','F'))
    closeDB(cs,conn)

def selectALLDB(tbname):
    conn = connectDB() #db 연결함수 호출  
    cs=conn.cursor() # 실행선언
    sql="select * from "+tbname
    rows = cs.execute(sql)
    print('-'*60)
    print('번호','이름','주소','전화번호','생일','성별',sep='\t')  
    print('-'*60)
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],sep='\t')  
    closeDB(cs,conn)
    
def selectDB(tbname,colname,val):
    conn = connectDB() #db 연결함수 호출  
    cs=conn.cursor() # 실행선언
    sql="select * from "+tbname+" where lower("+colname+ ") like '%"+val.lower()+"%'"
    rows = cs.execute(sql)
    print('-'*60)
    print('번호','이름','주소','전화번호','생일','성별',sep='\t')  
    print('-'*60)
    for row in rows:
        print(row[0],row[1],row[2],row[3],row[4],row[5],sep='\t')  
    closeDB(cs,conn)    

def modifyDB(tbname,id,colname,val):
    conn = connectDB()#db 연결함수 호출  
    cs=conn.cursor() # 실행선언
    
    sql = "update "+tbname+" set "+colname+"='"+val+"' where sno="+str(id)
    cs.execute(sql)
    closeDB(cs,conn)

def deleteDB(tbname,id):
    conn = connectDB()#db 연결함수 호출  
    cs=conn.cursor() # 실행선언
    sql = "delete from "+tbname+ " where sno=" +str(id)
    cs.execute(sql)
    closeDB(cs,conn)
    
    
def insertDBwithList(tbname,lis): # insert 하기 
    conn = connectDB() #db 연결함수 호출  
    cs=conn.cursor() # 실행선언
    # stumem -> sno, sname, sadd, sphone, sbirth, gender
    sql="insert into "+ tbname +" values(st_seq.nextval,:1,:2,:3,:4,:5)"
    cs.execute(sql, (lis[0],lis[1],lis[2],lis[3],lis[4]))
    closeDB(cs,conn)
    
        
    
# createTableDB("stumem") 
# insertDB("stumem")
# selectDB("stumem",'sname','홍')
# modifyDB("stumem",3,"sphone","81+32222222")
# deleteDB("stumem",3)

# lis = ['이순신','서울시 종로구','01055555555','20050505','M']
# insertDBwithList("stumem",lis)



selectALLDB("stumem")