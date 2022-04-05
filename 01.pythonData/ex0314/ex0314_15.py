aa = []
bb = []

# # 2의 배수
# for i in range(100):
#     aa.append(i*2)

# print(aa)

# for j in range(100):
#     bb.append(aa[99-j])
    
# print(bb)

# 3의 배수 200 개 
for i in range(200):
    aa.append(i*3)
print(aa)
for j in range(200):
    bb.append(aa[199-j])
print(bb)

print(aa[10:25])  # 10 에서 25까지
print(aa[:32])    # 0 에서 32 까지
print(aa[100:])   # 100 부터 끝까지 
print(aa[190:220])# 있는 값까지 
print(aa[-7:])# 뒤에서부터 출력
print(aa[190:-5])#  