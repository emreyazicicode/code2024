import random







# RANDOM NUMBER GUESS GAME



son_temp = 1

def termometreden_oku():
	global son_temp
	rasgele = random.randint( son_temp, 20) # Returns a number between 1 and 15
	son_temp = rasgele # save the variable value to "GLOBAL", so we dont forget
	return rasgele # we forget the "rasgele" variable

temperature = termometreden_oku() # 5
print('starting with', temperature)
while temperature < 15:
	print(temperature, 'running the heater')
	print('vakit gecti..... time passed')
	temperature = termometreden_oku()
	print('tekrardan olcum yaptik', temperature)
	



# SCOPE
# Variables have SCOPES
def someoperation():
	a = 1
	print("a", a)

a = 2
print("a", a)





# GLOBAL SCOPE
b = 2
print("b", b)

# SCOPE
# Variables have SCOPES
def myfunction1():
	# FUNCTION SCOPE
	print("b", b)  # 
	c = 4
	#! b = 16 X XXXXXX

def myfunction2():
	# FUNCTION SCOPE
	print("b", b)  # 
	c = 5


# PI = 22.0 / 7.0
# PI = 3.00
PI = 3.14

def dairealanhesapla( r: int ):
	return PI * r * r

def dairecevrehesapla( r: int ):
	return 2 * PI * r

print( "Dairenin cevresi budur: ", dairealanhesapla(3) )

def f(x):
	return x + 1

y1 = f( 3 )
y2 = f( 9 )
y3 = f( 0 )
y4 = f( -1 )
print(y1, y2, y3, y4)


def cevreHesapla( uzunluq, en ):
	#...
	#...
	#...
	#...
	return 2 * (uzunluq + en)

qqq = cevreHesapla( 10, 7 )
print(qqq)



print(cevreHesapla( 3, 10 ))
print(cevreHesapla( 4, 10 ))

en = 3
uzunluq = 10
print( (en + uzunluq) * 2 )

en =4
uzunluq = 10
print( (en + uzunluq) * 2 )

en = 5
uzunluq = 10
print( (en + uzunluq) * 2 )

en = 6
uzunluq = 10
print( (en + uzunluq) * 2 )


machineprice = 3
machine_price = 3
machinePrice = 3 # camelCase

# In file, function, variable names, DO NOT USE keywords (! and, list, is, as ....)
# https://www.w3schools.com/python/python_ref_keywords.asp

def masinQiymet( km, year, mark, model, auto, crash, fueltype, color ):
	
	# return 1 * .sdfadfdsa fdsafafds fafsd
	pass


result = masinQiymet( 10000, 2010, 'Mazda', 'RX-7', True, 0, 'Fuel', 'White' )


def masinQiymet2( parameters: dict ):
	parameters['km']
	pass



mymachine = {
	'km': 10000,
	'year': 2010,
	'mark': 'Mazda',
	#.....
}
result = masinQiymet2( mymachine )





def masinQiymet3( km, year, mark, model, auto, crash, fueltype, color ):
	#* some operations
	#* some more operations
	pass





def crashZarar( original, crash ):
	if crash < 1000:
		return original - crash
	elif crash < 5000:
		return original - crash * 2
	else:
		return original - crash * 3



print( crashZarar( 50000, 7500 ) )


import math

#math.
print("=" * 80)

print( round( 3.5 ))
print( round( 3.2 ))
print( round( 3.0 ))
print( round( 3.9 ))

print( round( 3.9, 0 ))


print( round( 3902.346, 2 ))

print("=" * 80)

def cevreHesapla2( r, pi = 3.14 ):
	return 2 * pi * r

print(cevreHesapla2(10))
print(cevreHesapla2(10, 3.14))
print(cevreHesapla2(10, 3))






a = 0
b = 0.0
c = ""
d = []
e = False
f = {}
g = ()
h = None # object # NULL, EMPTY, NILL, null


if b  > 4452:
	a = 3243
else:
	a = 4243

