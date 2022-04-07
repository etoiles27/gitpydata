import datetime

now = datetime.datetime.now()
mm = now.strftime('%m')
dd = now.strftime('%d')
print(mm)
print(dd)