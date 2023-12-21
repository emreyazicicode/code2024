
# python ozu
import math
import random
import time
import os
import sys
import datetime # import








d2 = datetime.date( 2017, 1, 17 ) # SADECE DATE, DATE ONLY

d = datetime.datetime(2017, 1, 17) # 17 Janvar 2017 00:00:00
d = datetime.datetime(2017, 1, 17, 12, 34, 58) # 17 Janvar 2017 12:34:58

print(d, type(d))
print(d2, type(d2))

# EXTRACING NECESSARY INFORMATION FROM A GIVEN DATE
print("YEAR  ", d.year)
print("MONTH ", d.month)
print("DAY   ", d.day)
print("HOUR  ", d.hour)
print("MINUTE", d.minute)
print("WEEKD ", d.weekday()) # HAFTANIN HANGI GUNU
print("MSECON", d.microsecond)
print("LAST D", d.day >= 25)


# 13 01 2017 # EXPORTING/CONVERTING A DATE TO A STRING 
# 2017 01 13

d = datetime.date(2017, 1, 20) # CONSTRUCT EDERKEN, Y,M,D
print(d.strftime("%d-%m-%Y"))
print(d.strftime("%Y-%m-%d"))
print(d.strftime("%Y-%b-%d"))
print(d.strftime("%d of %b %Y, %A"))



# date of birth
now = datetime.datetime.now()
dob = datetime.datetime(1985,1,24)
age = now.year - dob.year
print(f"Ahmet in yasi {age}")


ts = now - dob
print("TIMESPAN", ts, type(ts)) # TIMESPAN = Difference between two dates


"""
for i in range(1000):
    now = datetime.datetime.now()
    print(now, now.microsecond)
"""



customer_Ali_buy_dates = [
    {"total": 120, "date": datetime.date(2023, 5, 7)},
    {"total": 20, "date": datetime.date(2023, 5, 17)},
    {"total": 80, "date": datetime.date(2023, 6, 6)},
    {"total": 55, "date": datetime.date(2023, 6, 25)},
    {"total": 47, "date": datetime.date(2023, 6, 13)},
    {"total": 10, "date": datetime.date(2023, 7, 29)},
    {"total": 100, "date": datetime.date(2023, 8, 30)},
    {"total": 250, "date": datetime.date(2023, 9, 1)},
    {"total": 500, "date": datetime.date(2023, 10, 4)},
]

#! TOTAL SALES
#! TOTAL NUMBER OF ITEMS, FREQUENCY
#! RECENT DATE

