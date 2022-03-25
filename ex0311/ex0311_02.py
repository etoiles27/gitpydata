import datetime

#날짜를 가져온다 .
 
now = datetime.datetime.now() #현재  날짜, 시간을 가져온다. 

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# 12월 1월 2월 - 겨울 , 3 4 5 봄, 678 여름 91011 가을 출력

thismonth = now.month

# thismonth = int(input('enther the month : '))

if 2<thismonth<6:
    print("봄")
elif 5<thismonth<9:
    print('여름')
elif 8<thismonth<12:
    print('가을')
else:
    print('겨울')
