# # 변수
# a,b,c,d,e,f,g,h,i,j,k = 0,0,0,0,0,0,0,0,0,0,0

# # 리스트
# a1 = [0,0,0,0,0,0,0,0,0,0,0]
# arr = [0 for i in range(10)]

arrlist = [i for i in range(10)]

print(arrlist)
print(arrlist[6])
# arrlist 속 수 더하기 
sum = 0
for i in arrlist:
    sum += arrlist[i]
    print(arrlist[i],end=' ')
print()
print(sum)
