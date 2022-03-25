# # 재귀함수
# def count(num):
#     if num>=1:
#         print(num,end=' ')
#         count(num-1)
#     else:
#         return

# count(20)
# map -> 리스트를 만들어주는 형태
# map(함수,리스트)


def plus10(n):
    return n+10

pl10 = lambda n: n+10

list1 = [1,2,3,4,5,6,7,8,9,10]

# for i in range(len(list1)):
#     list1[i]=pl10(list1[i])
# print(list1)

print(list(map(plus10,list1)))

print(list(map(lambda n: n+10,list1)))
print(list(map(lambda n1,n2,n3: n1+n2+n3,list1,list1,list1)))


# 데이터 값을 넘겨준다. 맞다틀리다.
print(list(map(lambda n:n>5,list1)))
#데이터 자체를 받고싶을때 filter 해당되는 데이터 값만들고온다
print(list(filter(lambda n:n>5,list1))) 

print(list(filter(lambda n:n%2==0,list1))) 


list2 = [0,1,0,0,1]
list3 = ['','aa','','','b']

for i in list3:
    if i:
        print(i,'True')
    else:
        print(i,'False')

for i in range(5):
    if list2[i]:
        print(list2[i])