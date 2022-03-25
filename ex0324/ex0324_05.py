import student

stuSave = []

# while True:
    
#     sCount=int(input("번호 (종료 0)>>"))
#     if sCount==0:
#         break
#     sName=input("이름 >>")
#     kor=int(input("국어점수 >>"))
#     eng=int(input("영어점수 >>"))
#     temp=student.Student(sCount,sName,kor,eng)
#     stuSave.append(temp)

stuSave.append(student.Student(1,'홍길동',100,100))
stuSave.append(student.Student(2,'이순신',100,100))    


    
tempName = input('홍길동의 이름을 변경하세요 >> ')
stuSave[0].setStuName(tempName)    
# 수정 
temp=int(input('홍길동의 국어점수를 변경하세요 >>'))
# 홍길동과, 이순신을 넣었다 가정 . 
stuSave[0].setKor(temp)

print('번호','이름','국어','영어','합계','평균','등수',sep='\t')    
for stu in stuSave:
    print(stu)