






#* EVERY TIME THE PROGRAM ENDS, ALL VARIABLES DIE!! LOST, ERASED, DESTROYED




import redis
MEMORYDATABASE = redis.Redis()

D = {}

# D['A'] = 10
#print(D['A'])
print(D)

#! MEMORYDATABASE.set( 'A', 10 ), HAFIZAYA (MEMORY) YAZDIM (WRITE)

print(MEMORYDATABASE.get('A').decode())

#a = 3
#print(a)




# close - exit - terminate 