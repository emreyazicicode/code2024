# 1. method of importing a library
import math

# In some cases, ten to power N is represented as "3E10" ==> 30000000000
# In some cases, numbers like 6.123233995736766e-17  ===> corresponds to `0`

print( math.cos( math.pi / 2 ) )

print(math.pi)

print( math.factorial( 5 ) )

print( math.pow( 5, 3 ) )

print( math.sqrt( 2 ))

print( math.log( 5000 ) )

"""
140m2   300000

0m2     600000
600000 / 0 =~ 

160m2   450000
....
....


"""


# math.inf
#! a = 3 / 0 error



# 2. method of importing a library
import math as mt

# 3. method of importing a library
#! from math import *

# 4. method of importing a library
from math import cos, sin


# Importing "oz" library
import ozkutuphane as oz
#print( ozkutuphane.mToCm(1) )

print( oz.mToCm( 3 ) )




def makeApplication( age, grade ) -> bool:
    assert age >= 17
    # some operations
    pass


def canMarry( info: dict ) -> bool:
    assert info['age'] >= 18
    assert info['married'] == False


age = 19
grade = 70
result = makeApplication( age, grade )


person = {
    'name': 'Anvar',
    'age': 30,
    'married': True
}

#! canMarry( person )



if ".tr" in "mustafaozturk@hotmail.com.tr":
    print('bu bir TR domain adi')


Extensions = ['com', 'net', 'org', 'edu']
if 'com' in Extensions:
    print('valid extension')
