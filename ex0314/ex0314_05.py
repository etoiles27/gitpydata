# 변수가 한개일때. 바로 데이터를 메모리에 넣는다. 
a = 1
b = 2 
c = a 
print(a,end=' ')
print(b,end=' ')
print(c)
# 문제가 되지 않는다 
a = 2
print(a,end=' ')
print(b,end=' ')
print(c)

# list의 경우
# list안에는 여러가지의 데이터가 들어 갈 수 있다. 
# 때문에 , 주소 값이 할당이된다. 
# copy 명령어를 통해서 메모리를 할당하게 해야함. 
# 단순복사는 주소값이 복사가 된다 
a = [1]
b = [2]
c = a 
print(a,end=' ')
print(b,end=' ')
print(c)
a[0] = 10
print(a,end=' ')
print(b,end=' ')
print(c)
# 포인터의 개념으로 리스트 복사를 하면 주소 복사가 된다. 