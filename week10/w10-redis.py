


#* KEY VALUE MEMORY STORAGE
#* DICT, MEMORY [FAST] STORAGE

import redis

#* Open a connection to "REDIS application"
R = redis.Redis()


#* It has inserted the redis memory as "customer1-balance" to "100.000manat"
#* set = write
R.set('customer1-balance', '100.000manat')

#* get = read
print(R.get('customer1-balance').decode())

"""
#* Writing
i = '100.000manat'
#* Reading
print(i)
"""
#! variable "i" is deleted

Row ==> transform

DL = 0.40
AL = 0.20
AB = 0.35


