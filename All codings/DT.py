from datetime import date
import time as t
startTime = t.perf_counter()

d = date(2000, 1, 22)
print(d)

endTime = t.perf_counter()
print("Duration : ", endTime-startTime)
