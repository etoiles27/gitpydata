# 학생성적프로그램 
import cx_Oracle


def myConn(): # db 연결 함수
    conn =cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
    return conn

def closeDB(cs,conn): # db 저장하고 연결 끊기. 
    cs.close()
    conn.commit()
    conn.close()

def stuInsert(): # db에 학생 성적을 입력하는 함수 
    conn=myConn() 
    cs=conn.cursor()
    
    # 사용자에게 학생이름과, 성적을 입력받는다. 
    print('-'*25)
    print("[ 학생성적 입력 ]")
    print('-'*25)
    stuname = input("학생의 이름을 입력해주세요 >> ")
    kor = int(input("국어성적을 입력해주세요 >> "))
    eng = int(input("영어성적을 입력해주세요 >> "))
    math = int(input("수학성적을 입력해주세요 >> "))
    # 입력받은 점수로 총점과 평균을 계산
    total = kor+eng+math
    avg = total/3
    
    # sql - insert 구문을 입력해서 db에 입력 rank = 1 로 채워준다 
    sql="insert into studata values(stu_seq.nextval,:1,:2,:3,:4,:5,:6,1)"
    rows=cs.execute(sql,(stuname,kor,eng,math,total,avg))
    
    # 만약 학생 정보가 입력되었을 경우 
    if cs.rowcount == 1:
        print("{} 학생정보가 성공적으로 저장되었습니다".format(stuname))
    else:
        print("오류가 발생하여 저장되지 않았습니다. ")
 
    # db 닫기 
    closeDB(cs,conn)
    

def stuSelectAll(): # db에 입력된 성적을 출력하는 함수
    conn = myConn() #db연결 
    cs=conn.cursor()
    
    # SELECT * 구문으로 전체 학생 정보 출력 
    sql = "select * from studata"
    rows=cs.execute(sql)
    
    print('-'*25)
    print("[ 학생 전체 성적 출력 ]")
    print('-'*25)
    
    
    print('-'*60)
    print("{:5s}{:12s}{:4s}{:4s}{:4s}{:4s}{:5s}{:4s}".format('번호','이름','국어','영어','수학','합계','평균','등수') )
    print('-'*60)
    
    for row in rows:
        print("{:5s}{:15s}{:5s}{:5s}{:5s}{:8s}{:7s}{:3s}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7])))
    
    print('-'*60)
    # db 닫기 
    closeDB(cs,conn)
    

def stuSelectByName(): # db에 이름을 검색하여 출력하는 함수
    conn = myConn() #db연결 
    cs=conn.cursor()
    
    stuname = input("학생의 이름을 입력해주세요 >> ")
    
    # SELECT - where 을 사용하여, 학생 이름을 입력받아 출력해준다.
    # like를 사용하여 검색한 문자가 들어 있는 모든 학생을 출력해준다. 
    # lower함수를 사용하여, 입력한 글자가 대소문자 구별없이, 그리고 입력된 학생이름 대소문자 구별없이 보여준다.
    
    sql =  "select * from studata where lower(stuname) like '%" +stuname.lower() +"%'"
    rows=cs.execute(sql)
    
    print('-'*25)
    print("[ 학생 성적 출력 ]")
    print('-'*25)
    
    print('-'*60)
    print("{:5s}{:12s}{:4s}{:4s}{:4s}{:4s}{:5s}{:4s}".format('번호','이름','국어','영어','수학','합계','평균','등수') )
    print('-'*60)
    
    for row in rows:
        print("{:5s}{:15s}{:5s}{:5s}{:5s}{:8s}{:7s}{:3s}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7])))
    
    print('-'*60)
    
    # db 닫기 
    closeDB(cs,conn)

def stuUpdate(): # 학생정보를 수정하여 db에 update하는 함수
    print('-'*25)
    print("[ 학생 성적 수정 ]")
    print('-'*25)
    
    # 이름 검색을 통해 보여주는 함수를 이용    
    stuSelectByName()
    
    conn = myConn() #db연결 
    cs=conn.cursor()
    
    stuno = input("수정을 원하시는 학생의 번호를 선택해주세요. >>")
    sql =  "select * from studata where stuno='" +stuno +"'"
    rows=cs.execute(sql)

    kor, math, eng = '0','0','0'
    stuname=''
    
    # 수정하고싶은 학생의 정보를 rows로부터 가져와 변수에 저장한다. 
    for row in rows:
        kor = row[2]
        eng = row[3]
        math = row[4]
        stuname=row[1]
        
        
    # 어떤 점수를 수정할 지 선택
    print('1.국어점수 수정')
    print('2.영어점수 수정')
    print('3.수학점수 수정')
    subnum = int(input("원하는 번호를 선택해주세요 >>"))
    
    
    if subnum == 1: # 국어점수 수정
        # 변경할 국어점수, 변경된 총합, 변경된 평균을 update query를 통해서 수정
        print('[국어점수 수정]')
        print("현재 {} 학생의 국어점수는 {}입니다.".format(stuname,kor))
        up_kor = input("변경할 국어 점수를 입력해주세요 >> ")
        up_total = int(up_kor)+int(eng)+int(math)
        up_avg = up_total/3
        sql="update studata set kor=:1,total=:2, avg=:3 where stuno=:4"
        cs.execute(sql,(up_kor,up_total,up_avg,stuno))
        
    elif subnum == 2: # 영어점수 수정
        # 변경할 영어점수, 변경된 총합, 변경된 평균을 update query를 통해서 수정
        print('[영어점수 수정]')
        print("현재 {} 학생의 영어점수는 {}입니다.".format(stuname,eng))
        up_eng = input("변경할 영어 점수를 입력해주세요 >> ")
        up_total = int(kor)+int(up_eng)+int(math)
        up_avg = up_total/3
        sql="update studata set eng=:1,total=:2, avg=:3 where stuno=:4"
        cs.execute(sql,(up_eng,up_total,up_avg,stuno))
        
    elif subnum == 3: # 수학점수 수정
        # 변경할 수학점수, 변경된 총합, 변경된 평균을 update query를 통해서 수정
        print('[수학점수 수정]')
        print("현재 {} 학생의 수학점수는 {}입니다.".format(stuname,math))
        up_math = input("변경할 수학 점수를 입력해주세요 >> ")
        up_total = int(kor)+int(eng)+int(up_math)
        up_avg = up_total/3
        sql="update studata set math=:1,total=:2, avg=:3 where stuno=:4"
        cs.execute(sql,(up_math,up_total,up_avg,stuno))
        
    else:
        print('잘못입력하셨습니다. 상위메뉴로 이동합니다.')

    # db 닫기 
    closeDB(cs,conn)
    
    
    
    
    

def stuDelete(): # 학생을 검색해서 db에서 그 내용을 삭제하는 함수
    conn = myConn() #db연결 
    cs=conn.cursor()
    
    print('-'*25)
    print("[ 학생 전체 성적 삭제 ]")
    print('-'*25)
    
    # 이름 검색을 통해 보여주는 함수를 이용    
    stuSelectByName()
    
    # 동명이인의 경우를 생각해서, 학생 번호로 선택하게 한다. 
    stuno = input("원하시는 학생의 번호을 입력해주세요 >> ")
    print("{}번 학생이 선택되었습니다. ".format(stuno))
    flag = input("정말로 삭제를 하시겠습니까 ? (동의 : y)")
    if flag =='Y' or flag =='y':
        sql="delete from studata where stuno='"+stuno+"'"
        rows=cs.execute(sql)
        print("삭제되었습니다. ")
    else:
        print("삭제가 취소되었습니다. ")
    
    # db 닫기 
    closeDB(cs,conn)
    
    
def stuRank_python(): # 학생성적 등수 출력하는 함수 
    conn = myConn() #db연결 
    cs=conn.cursor()
    
    sql = "select * from studata order by stuno"
    rows=cs.execute(sql)
        
    totallist = []
    idlist = []
    ranklist=[]
    
    # 학생 번호 순서로 쿼리에서 가져와서 총점을 totallist 리스트에 넣는다 
    for row in rows:
        totallist.append(row[5])
        idlist.append(row[0])
    
    # ranklist에 등수를 계산해서 순서대로 넣는다. 
    rcount=0   
    for i in range(len(totallist)):
        rcount=1
        for j in range(len(totallist)):
            if totallist[i]<totallist[j]:
                rcount+=1
        ranklist.append(rcount)
    
    
    for k in range(len(totallist)):
        sql1 = "update studata set rank=:1 where stuno=:2"
        cs.execute(sql1,(ranklist[k],idlist[k]))
    
    
    print("등수반영이 완료되었습니다 ")
    # db 닫기 
    closeDB(cs,conn)
    
    
def stuRank(): # 학생성적 등수 출력하는 함수 
    conn = myConn() #db연결 
    cs=conn.cursor()
    
    sql = "update studata a set rank =(select rank from (select stuno, rank() over(order by total desc) as rank from studata) b where a.stuno = b.stuno)"
    cs.execute(sql)
    
    print("등수반영이 완료되었습니다 ")
    # db 닫기 
    closeDB(cs,conn)
    
    

#  main part 
while True:
    # 화면 출력 
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생 성적 입력') 
    print('2. 학생 성적 출력') 
    print('3. 학생 검색 출력') 
    print('4. 학생 성적 수정') 
    print('5. 학생 성정 삭제') 
    print('6. 학생 등수 처리')         
    print('0. 프로그램종료')   
    print('-'*25)
    # 숫자만 받는데, 문자를 입력하면 에러
    # 숫자만 받도록 변경
    choice = input('원하는 번호를 입력하세요.>>')
    if not choice.isdigit():  # 숫자
        print('숫자만 입력가능합니다.!!')
        break
        
    choice = int(choice)
    if choice == 1 : # 1. 학생성적입력
        stuInsert()
    elif choice == 2 : # 2. 학생성적출력
        stuSelectAll()
    elif choice == 3 : # 3. 학생검색출력
        stuSelectByName()
    elif choice == 4 : # 4. 학생성적수정
        stuUpdate()    
    elif choice == 5 : # 5. 학생성적삭제
        stuDelete()  
    elif choice == 6 : # 6. 학생등수처리
        stuRank()
    elif choice == 0 : #0. 프로그램종료
        print('프로그램을 종료합니다. ')
        break
    else:
        pass