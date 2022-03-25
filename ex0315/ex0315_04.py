
students = [
    [1,'홍길동',100,100,200,100.0,0],
    [2,'이순신',100,100,200,100.0,0],
    [3,'유관순',100,100,200,100.0,0],
    [4,'김유신',100,100,200,100.0,0],
    [5,'김구',100,100,200,100.0,0]
]

# for stu in students:
#     for s in stu:
#         print(s, end='')
#     print()

# ck_name = input('찾는 학생 이름을 입력하세요  >>  ')
# for idx, stu in enumerate(students):
#     if ck_name in stu:
#         del(students[idx])
#         # # 찾는학생 출력 
#         # for s in stu:
#         #     print(s, end='')
#         # print()
#         # #print(stu)
#         # break
        
# print(students)


while True:
    ck_name = input('찾는 학생 이름을 입력하세요  >>  ')
    for idx, stu in enumerate(students):
        if ck_name in stu:
            del(students[idx])    
    print(students)