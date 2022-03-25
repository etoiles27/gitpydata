aa = [1,2,3]
bb = [4,5,6]

cc = aa + bb # 리스트 합치기
print(cc)

dd = aa*3  # aa를 반복적으로 3번 합친것 
print(dd)

print(cc[::2])
print(cc[::-2])

cc[0] = 10 
cc[1:2] = [20,21]
cc[1:3]=[50,40,30,20]


cc[5] = [1,2,3]

print(cc)

del(cc[0])
print(cc)