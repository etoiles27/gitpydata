str1 = '1,홍길동,100,100,200,100.0,0'

data1 = str1.split(',')

print(data1)
# if '홍길동' in str1:
#     print("있어")


str2 ='2       유관순  100     100     200     100.0   0'
str3 = str2.replace(' ','')

print(str2)
print(str3)
data2 = str3.split(',')
print(data2)