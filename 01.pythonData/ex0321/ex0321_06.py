# list1 = [1,2,3]
# list2 = list1 
# list2[0]=100
# print(list1[0])


# 지역변수와 전역변수 
def cal1(a,b):
    result = 0
    result = a+b
    a=100
    b=200
    return result

def cal2(a,b):
    result = 0
    result = a+b
    a=1
    b=2
    return result


a = 20
b = 10

cal1(a,b)
cal2(a,b)
print('a,b의 값 : ',a,b)