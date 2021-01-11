import datetime

now = datetime.datetime.now()
print(now)  # 2021-01-11 23:16:20.590214
print(now.isoformat()) # 2021-01-11T23:16:20.590214
print(now.strftime('%d/%m/%y-%H%M%S%f')) # 11/01/21-231620590214

today = datetime.date.today()
print(today) # 2021-01-11
print(today.isoformat()) # 2021-01-11
print(today.strftime('%d/%m/%y')) # 11/01/21

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t) # 01:10:05.000100
print(t.isoformat()) # 01:10:05.000100
print(t.strftime('%h_%M_%S_%f')) # Jan_10_05_000100

print(now)
#6d = datetime.timedelta(weeks=1)
#d = datetime.timedelta(days=365)
#d = datetime.timedelta(hours=1)
d = datetime.timedelta(minutes=1)
print(now - d)

import time 
print("###")
time.sleep(2)
print("###")

import os
import shutil

file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))

with open(file_name, 'w') as f:
    f.write('test')

