
# print('*')
# print('*'*2)
# print('*'*3)
# print('*'*2)
# print('*')

# for i in range(1,11):
#     print('*'*i)
    
# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print('-'*j,end='')
#     print('*'*i)
    
i = 10

while i>=0:
    j = 0 
    while j<i:
        print('*',end='')
        j +=1
    print()
    i -=1
    
# 왼쪽 삼각형 
for i in range(1,11):
    print('*'*i)

# 오른쪽 삼각형 
for i in range(1,11):
    print(' '*(10-i)+'*'*i)

#역삼각형
for i in range(1,11):
    print('*'*(10-i)+' '*i)

# 가운데 삼각형
for i in range(1,11):
    print(' '*(10-i)+'*'*(2*i-1))
