# def cal1():
#     global a
#     a = 10 
    
# a = 20 

# cal1()
# print(a)

#함수선언

# def calc(v1,v2):
#     calList = []
#     calList.append(v1+v2)
#     calList.append(v1-v2)
#     return calList


# myList = []
# hap, sub = 0,0

# myList = calc(100,200)
# hap = myList[0]
# sub = myList[1]
# print('100+200 = {} \n100-200 = {}'.format(hap,sub))

# # global변수를 사용했을 때 
# def calc(v1,v2):
#     global hap, sub
#     hap = v1+v2
#     sub = v1-v2

# hap, sub = 0,0
# myList = calc(100,200)

# print('100+200 = {} \n100-200 = {}'.format(hap,sub))


# list 를 사용할 경우 - global 선언 없이 사용할 수 있다. 

def calc(v1):
    temp1 = v1[0]
    temp2 = v1[1]
    v1[0] = temp1 + temp2
    v1[1] = temp1 - temp2
 
myList = [100,200]
# 함수호출
calc(myList)
print('100+200 = {} \n100-200 = {}'.format(myList[0], myList[1]))