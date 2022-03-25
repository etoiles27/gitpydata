# import datetime as dt
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.minute
sec = now.second

print("{}-{}-{} {}:{}:{}".format(year,month,day,hour,min,sec))
print(now)

# stuSave = []
# stu_name = input('이름을 입력하세요 >> ')
# now = datetime.datetime.now()
# nnow = now.year
# temp={'stuname':stu_name,'inputtime':'{}'.format(now)}
# stuSave.append(temp)
# print(stuSave)


