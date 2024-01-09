













import redis
MEMORYDATABASE = redis.Redis()


print(MEMORYDATABASE.get('A').decode())


# MEMORYDATABASE.set('name', 'Ali', 10)

#print(MEMORYDATABASE.get('name').decode())


def fillMemory():
    MEMORYDATABASE.set( 'YEAR2023PROFIT', 231543210 )
    MEMORYDATABASE.set( 'YEAR2022PROFIT', 93425359 )
    MEMORYDATABASE.set( 'YEAR2021PROFIT', 63924039 )
    MEMORYDATABASE.set( 'YEAR2020PROFIT', 14990566 )

# fillMemory()

number_of_employees = 1203
print( "YEAR2023PROFIT", int(MEMORYDATABASE.get('YEAR2023PROFIT').decode()))

print( "Profit per employee", int(MEMORYDATABASE.get('YEAR2023PROFIT').decode()) / number_of_employees )

import time


starttime = time.time()
for i in range(100000):
    x = int(MEMORYDATABASE.get('YEAR2023PROFIT').decode())
endtime = time.time()


print(endtime - starttime)


