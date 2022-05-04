# 함수선언 def 함수이름(매개변수1, 매개변수2, .....)
# return은 함수를 호출한 곳으로 값을 돌려준다. 생략가능
# 함수 내 변수는 지역변수. 
# 
# 함수에서 매개변수의 개수는 동일해야한다. 
# 매개변수의 개수를 맞추지 않으면 error 
# type은 상관없다.

# def para_func(v1,v2,v3=0): # 매개변수 기본값 (변수가 들어 오지 않을때 기본값으로 설정됨)
#     result = 0
#     result = v1+v2+v3

#     return result

 
# hap = para_func(1,2)

# print(hap)



# 기본값 매개변수를 사용해서 
# 3개 변수를 받는 함수를 선언하고
# v1,v2,v3 +-*/, v3기본값은 1 
# 4개의 값을 리턴받아서 전역부분에서 출력하세요 
# 함수 cal1(1,2) cal2(20,1,5), cal1(100,5)

def cal1(v1,v2,v3=1):
    result=[]
    result.append(v1+v2+v3)
    result.append(v1-v2-v3)
    result.append(v1*v2*v3)
    result.append(v1/v2/v3)
    return result

r = cal1(1,2)
print('1+2+1={} 1-2-1={} 1*2*1={} 1/2/1={}'.format(r[0],r[1],r[2],r[3]))

r = cal1(20,1,5)
print('20+1+5={} 20-1-5={} 20*1*5={} 20/1/5={}'.format(r[0],r[1],r[2],r[3]))

r = cal1(100,5)
print('100+5+1={} 100-5-1={} 100*5*1={} 100/5/1={}'.format(r[0],r[1],r[2],r[3]))