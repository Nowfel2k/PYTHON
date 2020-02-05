import re

str = "Take one idea, follow it with all your heart."

a = re.search(r'o\w+', str)
print(a.group())

b = re.findall(r'o\w\w', str)
print(b)

c = re.match(r'T\w', str)
print(c.group())

dat = 22-7-2000
datex = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', dat)

import datetime as d
import time as t

print(t.time())

DateTimeNow = t.ctime(t.time())
print(DateTimeNow)

b = d.datetime.today()
print(b)

print(b.hour, b.minute, b.second)
print(b.day, b.month, b.year)

if b.year%4==0:
    print("Leap Year")
else:
    print("Not leap")


