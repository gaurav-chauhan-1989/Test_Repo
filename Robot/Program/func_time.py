import time
import datetime

print(time.asctime(time.localtime(time.time())))
a=datetime.datetime.now()
print(a.strftime("%d:%m:%Y %H-%M-%S %p"))
print(a.strftime("%A %B"))
print(a.strftime("%a %b"))