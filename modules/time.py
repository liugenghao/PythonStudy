# Author:Bill Lew
import time,datetime

x = time.localtime()
print(x)
print("%s年%s月%s日" %(x.tm_year,x.tm_mon,x.tm_mday))
print("今天是%s年的第%s天" %(x.tm_year,x.tm_yday))

print(time.strftime("%Y-%m-%d",time.localtime()))
print(time.strptime("2018-03-04","%Y-%m-%d"))
print(datetime.datetime.now().strftime('%Y-%m-%d'))
print(datetime.datetime.now()+datetime.timedelta(-3))#前三天