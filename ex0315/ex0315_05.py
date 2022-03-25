
# 이름을 검색해서 삭제하는 프로그램
# 1 번 찾는 사람 검색 2 번 찾는 사람 삭제 

students = [
    [1,'홍길동',100,100,200,100.0,0],
    [2,'이순신',100,100,200,100.0,0],
    [3,'유관순',100,100,200,100.0,0],
    [4,'김유신',100,100,200,100.0,0],
    [5,'김구',100,100,200,100.0,0]
]

ans = 0 
while True:
    ans = int(input("학생 정보 검색 1번 \n학생 정보 삭제 2번 [종료: 0번]>> "))
    ck = 0
    if ans == 1:
        ser_name =  input('이름을 입력하세요 >>')
        
        for idx, stu in enumerate(students):
            if ser_name in stu:
                print(students[idx])
                ck = 1
                break
            if ck == 0 :
                print('존재하지 않는 학생입니다. ')
                break
        
    elif ans == 2:
        ck_name = input('이름을 입력하세요 >>')
        for idx, stu in enumerate(students):
            if ck_name in stu:
                del(students[idx])
                ck = 1
            if ck == 0:
                print('존재하지 않는 학생입니다. ')
                break
        print(students)
    elif ans == 0:
        break