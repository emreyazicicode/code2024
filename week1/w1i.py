
# variable

a = 3
b = "a"
c = 3 * 2
d = "a" + "c"
e = a + c
f = a
f = f + 1


g = 1  # Assign a "value 3 " to g
g = a  # Assign a value of a variable (a) to g

#if a = 3:
#    pass

if a == "3":
    print("a 3'e esittir")

# [string, int, bool, float], [list, tuple, dictionary]
"""
age = 18
if age >= 18:
    print('you can marry')
"""


"""
if temperature is less than 5 then "very cold"
if temperature is less than 10 then "cold"
if temperature is less than 20 then "average"
if temperature is less than 30 then "hot"
if above the last point then "very hot"
"""


temperature = 3

if temperature < 5:
    print("very cold")
elif temperature < 10:
    print("cold")
elif temperature < 20:
    print("average")
elif temperature < 30:
    print("hot")
else:
    print("very hot")


# if month == 12 or month == 1 or month == 2 then 'winter'
# if month is 3 or 4 or 5 then 'spring'
# if month is 6 or 7 or 8 then 'summer'
# if month is 9 or 10 or 11 then 'autumn'

month = 5
if month == 12 or month == 1 or month == 2:
    print('winter')
if month == 3 or month == 4 or month == 5:
    print('spring')
if month == 6 or month == 7 or month == 8:
    print('summer')
if month == 9 or month == 10 or month == 11:
    print('autumn')



month = 1
if month == 1:
    pass

if month in [12,1,2]:
    print('winter')


# 1- if, elif, else, def, for [keyword] ==> sonra ":" colon iki nokta
# 2- iki nokta dan sonraki satirda, mutlaka "TAB" olacak
# 3- MUKAYESE, COMPARE, CHECK gibi islemlerde "=="


saat = 12

# if saat in [23, 0, 1]
saatler = list(range(24))

if saat in saatler[1:4]:
    print('night')

saat = 15
if saat in range(12,16):
    print("OK")


if saat in [23, 0, 1]:
    print('gece')

if saat in range(16,19):
    print('aksam uzeri')

if saat == 12 or saat == 13:
    print('ogle vakti')

if saat > 12 and saat < 15: 
    print('ogleden sonra')

vakitler = {  0: 'gece',  1: 'gece',  2: 'gece',   18: 'aksam' }

sirali = [ 'gece', 'gece', 'gece', 'sunrise' ] # ...



print( vakitler[ 18 ] )
print( sirali[3])


