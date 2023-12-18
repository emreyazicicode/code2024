
#* Python [week2]
import pprint as pp

#* 
#*  Force = Mass x Acceralation
#*  f = m . a
#* 

def force( m, a ):
    return m * a

def fonksiyonName( argument1, argument2, argument3 ): #! < --- colon at the end
    #* Operations
    pass

#* When to write as a function
#* If we are going to use for more than once
#* We dont use, if we are going to use it "ONCE"


def fonksiyonName2( argument1: str ) -> int: #* They are not required
    # ......
    pass


#* V = x / t
#* Velocity (speed, HIZ) = YOL (ne kadar yol gittik) / TIME (ZAMAN) 
#* 100 metre = yol (road)...... 5 saniye (5 seconds) ==> OUR SPEED = 100 / 5 = (20metre/saniye)
#* Velocity = (metre/s)
#* Yol (x)  = Metre
#* Time     = Seconds, Saniye

def V( X, T ):
    return X / T

# Put the types
def V2( X: float, T: float ) -> float:
    return X / T

# Make lower case
def v( x: float, t: float ) -> float:  #! In parameter names, we dont use only a LETTER
    return x / t

# Change the name to more readable
def velocity( distance: float, time: float ) -> float:
    return distance / time

def velocity2( distance: float, time: float ) -> float:
    return distance / time

def velocity3( distance: float, time: float ) -> float:
    #* Check the arguments
    if not (type(distance) is float or type(distance) is int): 
        #* If the type of distance is not float or is not int
        return "ERROR"
    if not (type(time) is float or type(time) is int): 
        #* If the type of distance is not float or is not int
        return "ERROR"
    #* Check if the time is zero
    if time == 0: 
        return 0
    #* Make the calculation and return result
    return distance / time

print( "velocity3( 100, 5 )", velocity3( 100, 5 ) )
print( "velocity3( 100, 0 )", velocity3( 100, 0 ) )
print( "velocity3( 100., 5.0 )", velocity3( 100.0, 5.0 ) )
print( "velocity3( 'salam', 5 )", velocity3( "salam", 5 ) ) # 
print( "velocity3( 100, 'nicesin' )", velocity3( 100, "nicesin" ) ) #

a = 3
b = 3.0
#print( type(a), type(a) is int )
#print( type(b), type(b) is int )


#* Masin Hizi = 60KM / Saat (kilometre / saat)

# NOTE: This function only supports when the distance is "meters" and time is "seconds"
def velocity4( distance: float, time: float, unit: str = 'm/s' ) -> float:
    #* Check the arguments
    if unit not in ['km/h', 'm/s']: # if the unit is not any of them!
        return 'ERROR'
    if not (type(distance) is float or type(distance) is int): 
        #* If the type of distance is not float or is not int
        return "ERROR"
    if not (type(time) is float or type(time) is int): 
        #* If the type of distance is not float or is not int
        return "ERROR"
    #* Check if the time is zero
    if time == 0: 
        return 0
    #* Check if the unit is km/h
    if unit == 'km/h':
        distance = distance / 1000.0
        time = time / 3600.0
    #* Make the calculation and return result
    return distance / time


print( "velocity4(100, 5)", velocity4(100, 5) )
print( "velocity4(100, 5, 'm/s')", velocity4(100, 5, 'm/s') )
print( "velocity4(60000, 3600, 'km/h')", velocity4(60000, 3600, 'km/h') )
#* 60 bin metre gittik, 3600 saniye de gittik.
print( "velocity4(60000, 3600, 'km/s')", velocity4(60000, 3600, 'km/s') )





def V6( X, T ):
    return X / T

# method: velocity5
# Calculates the velocity of an object
# @distance, float: The distance travelled
# @time, float: The time passed
# @unit, str: The unit of the calculation
# @return, float: The result of the calculation (speed)
# @completed
def velocity5( distance: float, time: float, unit: str = 'm/s' ) -> float:
    #* Check the arguments
    if unit not in ['km/h', 'm/s']: # if the unit is not any of them!
        return 'ERROR'
    if not (type(distance) is float or type(distance) is int): 
        #* If the type of distance is not float or is not int
        return "ERROR"
    if not (type(time) is float or type(time) is int): 
        #* If the type of distance is not float or is not int
        return "ERROR"
    #* Check if the time is zero
    if time == 0: 
        return 0
    #* Check if the unit is km/h
    if unit == 'km/h':
        distance = distance / 1000.0
        time = time / 3600.0
    #* Make the calculation and return result
    return distance / time






def faizlariHesapla( faizler: list ) -> float:

    def neftFaizKontrol( faiz: float ) -> bool:
        if type(faiz) is str: return False # EGER FAIZ IN TYPE I STRING ISE FALSE DONDUR
        if faiz > 1.0: return False
        if faiz < 0.0: return False
        return True

    total = 0
    count = 0

    for faiz in faizler: #* HER BIR, HEPSI, ALL
        if neftFaizKontrol( faiz ) == True: #* EGER VALID
            total = total + faiz
            count = count + 1
            # print("AKTIF OLARAK EKLENEN", faiz, "TOTAL", total, "COUNT", count)
    
    return total / count

#* faiz = NEFT/STREAM [liquid] (socar) [soil, toprak, camur, su, neft]
#* faiz = Faiz (ratio)
faizler = [ 0.20, 0.30, 0.15, 0.19, 0.22, 0.50, 0.90, 0.80, 0.55, 1.12, 0.04, -0.05, "0", "SALAM"]
result = faizlariHesapla( faizler )
result = round(result, 3)
print(result)
#* Sensor ===> Sensor may have errors






#* optional parameters
#* istersek veri gireriz, girmezsek, default value kullanilir
def makeCake( fındıq: float = 0, qoz: float = 0, kakao: float = 0, üzüm: float = 0 ):
    
    assert fındıq is not None
    assert qoz is not None
    assert kakao is not None
    assert üzüm is not None

    #* piroq
    #* Flour alinir, karistirilir
    #* Isitilar
    # ....

    # 1. kutudan "su kadar" findiq al, tavaya koy
    # .....
    # ....
    # ....
    # Cake = mixture, kek, tort
    pass


makeCake( 100, 100, 50, 0 ) # findiqli, qoz, kakaolu
makeCake( 0, 100, 0, 100 )  # uzumlu, qoz
makeCake( 100, 100, 0, 0 )  # findiq, qoz
makeCake( 0, 0, 50, 100 )   # uzumlu, kakaolu
makeCake( 0, 0, 0, 0)       # SADE, yalin, simple

# SADECE UZUMLU PIROQ tapmak istiyorum
makeCake()

#* The lines below are SAME
makeCake( 0, 0, 0, 100 )
makeCake( üzüm = 100 )

#* COK PARAMETRE + COK OPTIONAL PARAMETRE
makeCake( kakao=100, qoz=100)
makeCake( 0, 100, 100, 0 )

a = 100 #! WRITES 100 onto variable "a"

# BELOW IS WRONG USAGE!
findik = 50
kakao = 100
makeCake( kakao, 50, findik, 20 )
#! The order of the parameters are important

#* COK PARAMETRE + COK OPTIONAL PARAMETRE
makeCake( kakao=100, qoz=100)
makeCake( 0, 100, 100, 0 )


#def makeClassification( treeDepth: int = 5, splitCount: int  = 2, ....... ):
#    pass
#makeClassification( splitCount = 3 )

# =============================================================================
#! lambda operator
# not or and 


def ftoc( fahrenheit ):
    return (fahrenheit - 32) / 1.8

#! EGER, BIR FUNCTION / METHOD, TEK BIR SATIRSA, SINGLE LINE (make operation and return)
#! O FONKSIYONU LAMBDA OLARAK TANIMLAYABILIYORUZ 
#! TEK FAIDESI: KULLANIM KOLAYLIK, KOLAY: EASE

ftoc2 = lambda fahrenheit: (fahrenheit - 32) / 1.8

print(ftoc( 500 ))
print(ftoc2( 500 ))


M2CM = lambda m: m * 100
L2CL = lambda l: l * 100
KMToMetre = lambda KM: KM * 1000

# Age = lambda DOB: NOW - DOB
#! TEK BIR SATIR, SINGLE LINE
#! FORMULLER
#! HESAPLAMALAR
#! DONUSUMLER

ManatToDolar = lambda Manat: Manat * 0.59
DolarToManat = lambda Dolar: Dolar * 1.70
Average = lambda Values: sum(Values) / len(Values)

print(Average([1,20,3,4,50]))

#FONKSIYONISMI = lambda INPUT: OPERATION

# below two statements are same
topla = lambda x, y: x + y

def topla2( x, y ):
    return x + y

#* KISALTMA == SHORTENING


# LAMBDA = 1 LINE (!!)

print('=' * 80)
# INLINE LAMBDA

a = 30
if a == 30: print('test')
elif a == 20: print('test2')
elif a == 10: print('test3')


if a == 30: 
    print('test')
elif a == 20: 
    print('test2')
elif a == 10: 
    print('test3')



point = 80
grade = None

if point >= 90: grade = 'A'
elif point >= 80: grade = 'B'
elif point >= 70: grade = 'C'
elif point >= 60: grade = 'D'
else: grade = 'E'


if point >= 90: 
    grade = 'A'
elif point >= 80:
    grade = 'B'
elif point >= 70: 
    grade = 'C'
elif point >= 60: 
    grade = 'D'
else: #* OTHER 
    grade = 'E'



# -----------------------------------------------------------------------------
point = 80
grade = 'E' # A, B, C, D, E

if point >= 90: grade = 'A'
elif point >= 80: grade = 'B'
elif point >= 70: grade = 'C'
elif point >= 60: grade = 'D'
# -----------------------------------------------------------------------------


point = 56
result = None
if point > 60:  # if ten sonra 1 tane 
    result = 'passed'
else: # else ten sonra 1 tane 
    result = 'failed'

print(point, result)


def checkPoint(point):
    if point > 60:  # if ten sonra 1 tane 
        result = 'passed'
    else: # else ten sonra 1 tane 
        result = 'failed'
    return result

# SINGLE LINE IF, IIF immediate if, lambda if
point = 56
result = 'passed' if point > 56 else 'failed' # SINGLE LINE
result2 = checkPoint(56)
print(result)
print("result2", result2)



#* Below statements are exactly same
checkPoint2 = lambda point: 'passed' if point > 60 else 'failed'


def checkPoint(point):
    if point > 60:  # if ten sonra 1 tane 
        result = 'passed'
    else: # else ten sonra 1 tane 
        result = 'failed'
    return result


def V9( X, T ):
    if T > 0:
        return X / T
    return 0

velocity10 = lambda x, t: x / t

velocity11 = lambda x, t: x / t if t > 0 else 0




print("velocity10 lambda", velocity10(100, 5))


#* store efficiency
#* total sales [300.000 manat]
#* personel staff count, employee count

store_efficiency = lambda total_sales, staff_count: int(round(total_sales / (staff_count + 1), -1))

#* b1     300.000  5     60.000
#* b2     250.000  3     80.000
#* b3     600.000  12    50.000
#* b4     450.000  7     64.500

print('*' * 80)
braches = [
    {'name': 'store1', 'total_sales': 300000, 'staff_count': 5}, # + 1 store manager 
    {'name': 'store2', 'total_sales': 250000, 'staff_count': 3}, # + 1 store manager 
    {'name': 'store3', 'total_sales': 600000, 'staff_count': 12},# + 1 store manager 
    {'name': 'store4', 'total_sales': 450000, 'staff_count': 7}, # + 1 store manager 
    {'name': 'store5', 'total_sales': 750000, 'staff_count': 10}, # + 1 store manager 
    {'name': 'store6', 'total_sales': 950000, 'staff_count': 13}, # + 1 store manager 
    {'name': 'store7', 'total_sales': 150000, 'staff_count': 2}, # + 1 store manager 
    {'name': 'store8', 'total_sales': 400000, 'staff_count': 8}, # + 1 store manager 
    {'name': 'store9', 'total_sales': 500000, 'staff_count': 9}, # + 1 store manager 
]

#* HER BIR TUMU HEPSI.... 
sum_eff = 0
for b in braches:
    #* Calculate the efficiency
    efficiency = store_efficiency( b['total_sales'], b['staff_count'] )
    sum_eff = sum_eff + efficiency # cumulative

print(sum_eff / len(braches))


#* HER BIR TUMU HEPSI.... 
calculated_efficiencies = []
for b in braches:
    #* Calculate the efficiency
    efficiency = store_efficiency( b['total_sales'], b['staff_count'] )
    calculated_efficiencies.append( efficiency )

average_efficiency = Average( calculated_efficiencies)

print("average_efficiency", average_efficiency)


for b in braches:
    efficiency = store_efficiency( b['total_sales'], b['staff_count'] )
    if efficiency < average_efficiency:
        print(b, efficiency)

efficiency_dictionary = {}
# dictionary = key, value

for b in braches:
    efficiency = store_efficiency( b['total_sales'], b['staff_count'] )
    efficiency_dictionary[ b['name'] ] = efficiency

pp.pprint(efficiency_dictionary)

#* BIR DICTIONARY ICINDE, LOOP YAPIYORUZ
for b in efficiency_dictionary: #* b ===> KEY
    print(b, efficiency_dictionary[b]) # b = key, efficiency_dictionary[b] = value


output = dict(sorted(efficiency_dictionary.items(), key=lambda item: item[1]))

print(output)
print('-' * 80)
print(efficiency_dictionary.keys())
print(efficiency_dictionary.values())
print(efficiency_dictionary.items())

#* [('store1', 50000), ('store2', 62500), ('store3', 46150), ('store4', 56250), ('store5', 68180), ('store6', 67860), ('store7', 50000), ('store8', 44440), ('store9', 50000)]
#* a list of tuples of [string and integer]
