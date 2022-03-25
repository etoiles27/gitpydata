from stumanage.student import Student

s1 = Student('홍길동',100,100)
s2 = Student('',0,0)
print(s1.stuname)

if s1==s2:
    print('동일인')
else:
    print('다른사람')
