
# # input은 입력 print는 출력

# a= input() # 인풋으로 입력받는것은 다 스트링이다 
# print(a)

id = 'admin'
pw = '1111'

student = []
students = []

stu_cnt = 1
# u_id = input('아이디를 입력하세요 : ')
# u_pw = input('비밀번호를 입력하세요 : ')

# 무한 반복 
while True:
    stu_no = stu_cnt #input('학생번호를 입력하세요 : ')
    print('학생번호 :' ,stu_cnt)
    stu_name = input('학생이름을 입력하세요 : ')
    kor = int(input('국어성적을 입력하세요 : '))
    eng = int(input('영어성적을 입력하세요 : '))
    math = int(input('수학성적을 입력하세요 : '))
    total = kor+eng+math
    avg = total/3
    rank = 0
    student=[stu_no, stu_name, kor, eng, math, total, avg, rank]
    students.append(student)
    stu_cnt += 1
    print(students)
        
        
    