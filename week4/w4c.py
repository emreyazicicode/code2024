"""
import json
mydatabase = {
    'a': 1,
    'b': 2.5,
    'c': 'test',
    'd': True
}
mydatabase['e'] = 'test222'
# SAVE TO FILE 
json.dump(mydatabase, open('w4.json', 'w'))

print(mydatabase)
"""

"""
import json
# LOAD FROM FILE
mydatabase = json.load(open('w4.json'))
print(mydatabase)
"""

import redis
MEMORYDATABASE = redis.Redis()

# WRITE TO MEMORY
# MEMORYDATABASE.set('a', 45)
# MEMORYDATABASE.set('b', 'selam')

print( MEMORYDATABASE.get('a').decode() )
print( MEMORYDATABASE.get('b').decode() )


MEMORYDATABASE.set( 'Ahmet', '12-12-2022' ) 
MEMORYDATABASE.set( 'Ahmet', '14-12-2022' ) 



#* SELECT AVG(rating) FROM ratings WHERE movie = 'Matrix' -> disk 
MEMORYDATABASE.set( 'Matrix', 4.7 ) 
MEMORYDATABASE.set( 'Too-Fast-Too', 4.1 ) 
#* DAILY UPDATE 



friends = (3, 2, 13, 26)

#* SELECT * FROM movie_watch WHERE user = 12342134

mylastmovies = {
    'matrix' : {'minute': 123, 'second': 48},
    'friends' : {'season': 3, 'episode': 1, 'minute': 13, 'second': 26},
    'cukur' : {'bolum': 13, 'minute': 123, 'second': 48}
}


MEMORYDATABASE.set( 'user12342134', '.........' )


