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


def f(x):
	return x + 1

y1 = f( 3 )
y2 = f( 9 )
y3 = f( 0 )
y4 = f( -1 )
print(y1, y2, y3, y4)


def cevreHesapla( uzunluq, en ):
	return 2 * (uzunluq + en)

qqq = cevreHesapla( 10, 7 )
print(qqq)

print(cevreHesapla( 10, 7 ))


