

aa =[10,20,30]
# 추가
aa.append(40)
# 변경
aa[0] = 100
aa[1:2] =[200,300] # 슬라이싱: 추가되면서 변경 
aa[1] = [1,2] # 리스트로 넣는다

print(aa)


students = [
    [1,'홍길동',100,100,200,100.0,0],
    [2,'이순신',100,100,200,100.0,0],
    [3,'유관순',100,100,200,100.0,0],
    [4,'김유신',100,100,200,100.0,0],
    [5,'김구',100,100,200,100.0,0]
]
# print(students)
# del(students[1])
# print(students)
# print(students[1])

# 전체 학생 출력
for stu in students:
    for s in stu:
        print(s,end=' ')
    print()

# 특정 학생 출력 

ck_name = input('찾는 학생이름을 입력해주세요 >> ')
tmp_ck = False   
for stu in students:
    if stu[1] == ck_name:
        print(stu)
        tmp_ck = True
        break
    else:
        continue

if tmp_ck == False:
    print('찾는 학생이 없습니다.')